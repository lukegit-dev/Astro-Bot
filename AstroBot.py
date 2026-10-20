import requests
import json
import os

from dotenv import load_dotenv
from datetime import datetime
from time import sleep

load_dotenv()

WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")
API_NINJAS_TOKEN = os.getenv("API_NINJAS_TOKEN")

# =========================
# CONFIGURATION FUNCTIONS
# =========================

BASE_WEBEX_URL = "https://webexapis.com/v1/"
BASE_OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/weather"
BASE_GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_REVERSE_GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/reverse"
BASE_ISS_URL = "http://api.open-notify.org/iss-now.json"
BASE_PLANETS_URL = "https://api.api-ninjas.com/v1/planets"

BOT_EMAIL = "Astraa@webex.bot"

def get_webex_token():  # Asks the user for a Webex token or uses a hardcoded one
    choice = input("Use hard-coded token? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ")
        return f"Bearer {token}"
    else:  # Hardcoded token
        return WEBEX_TOKEN
    
def get_api_key(hardcoded_key):
    choice = input("Use hard-coded API key? (y/n): ").lower()
    if choice == "n":
        return input("Enter your API Key: ")
    else:
        return hardcoded_key
    
# =========================
# WEBEX FUNCTIONS
# =========================

def get_rooms(token):
    """
    Example of a room element of what would be returned from fetching rooms
    {
        'id': 'XXXX',
        'title': 'Example Room', 
        'type': 'direct',
        'lastActivity': '2026-09-16T09:31:45.085Z',
        'creatorId': 'XXXX',
        'created': '2026-09-16T09:31:45.085Z',
        'ownerId': 'XXXX',
        'isPublic': False,
        'isReadOnly': False,
        'isLocked': False
    }
    """
    url = BASE_WEBEX_URL+"rooms"  # URL to fetch rooms from Webex API
    headers = {'Authorization': token}  # Include Authorization in headers
    response = requests.get(url, headers=headers)  # Get rooms using requests.get with the url and headers

    if response.status_code != 200:  # Check if the response status code is not 200
        print("Error fetching rooms. ERROR CODE", response.status_code)
        return None

    return response.json().get("items", None)  # Attempts to get "items" from JSON response. Returns empty list if not found.

def print_rooms(rooms):
    for room in rooms:
        print(f"Room Name: {room['title']} | ID: {room['id']}")

def select_room(rooms):
    while True:
        
        print("Enter the room number you wish to connect to.\n")

        for i, room in enumerate(rooms):  # Displays a list of room numbers and correlating room name
            print(f"{i+1}. {room['title']}")

        try:
            number = int(input("\n: "))  # Converts answer to int

            if 1 <= number <= len(rooms):  # Checks if users number is within range of rooms available / displayed
                room = rooms[number - 1]  # Python starts indexing at zero for its first value
                print(f"Selected Room: {room['title']}")
                return room['id']
            
        except ValueError:
            print("Room has to be a whole number!")
            continue

        print("Room not found!")

def get_latest_message(token, room_id):
    url = BASE_WEBEX_URL+"messages"  #  https://webexapis.com/v1/messages
    params = {'roomId': room_id, 'max': '20'}  # Use 'roomId' and 'max' parameter to fetch the room and limit the number of messages returned to 20
    headers = {'Authorization': token}  # Use auth token in headers with our request

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Error fetching messages. ERROR CODE", response.status_code)
        return None, None

    data = response.json().get("items", None)  # tries to get items table, if it fails, return None

    if not data:  # Fails
        return None, None
    
    latest = data[0]

    if latest.get("personEmail") == BOT_EMAIL:  # Stops the bot from responding to its own messages
        return None, None

    return latest.get("id"), latest.get("text", "")

def send_message(token, room_id, message):
    url = BASE_WEBEX_URL+"messages"
    headers = {'Authorization': token, 'Content-Type': 'application/json'} # Authorization header (token) and Content-Type as application/json to be included on request.post()
    data = {
        "roomId": room_id,
        "text": message
    }
    requests.post(url, headers=headers, data=json.dumps(data))

# =========================
# WEATHER FUNCTIONS
# =========================

def get_city_coordinates(city, api_key):
    params = {'q': city, 'limit': 1, 'appid': api_key}  # City name, limit, and the API key in params
    response = requests.get(BASE_GEOCODING_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if location is None:
        print("No weather data found")
        return {'error': 'No city data found.'}  # if .get() fails, return an error message as a fallback

    params = {'lat': location['lat'], 'lon': location['lon'], 'units': 'metric', 'appid': api_key}  # latitude, longitude, units as metric, and the API key

    response = requests.get(BASE_OPENWEATHERMAP_URL, params=params)

    if response.status_code != 200:  # The response was unsuccessful
        print("No weather info found, status code error:", response.status_code)
        return {'error': 'Weather data is unavailable'}  # if .get() fails, return an error message as a fallback

    weather = response.json()

    # Return the weather information including city name, country, temperature, weather description, humidity, and wind speed
    
    return {
        'city': weather['name'],
        'country': weather['sys']['country'],
        'temperature': weather['main']['temp'],
        'description': weather['weather'][0]['description'],
        'humidity': weather['main']['humidity'],
        'wind_speed': weather['wind']['speed']
    }

# =========================
# PLANET INFO FUNCTION
# =========================

def get_planet_information(planet_name, api_key):
    
    response = requests.get(
        BASE_PLANETS_URL,
        headers={'X-Api-Key': api_key},
        params={'name': planet_name}
    )
    if response.status_code == 200:
        return response.json()
    else:
        print("Error with fetching planet information:", response.status_code, response.text['error'])
        return None

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    params = {'lat': lat, 'lon': lon, 'limit': 1, 'appid': api_key}  # params including the latitude, longitude, limit, and the API key

    response = requests.get(BASE_REVERSE_GEOCODING_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):

    response = requests.get(BASE_ISS_URL)  # http://api.open-notify.org/iss-now.json

    if response.status_code != 200:
        return 'No ISS location data found'

    data = response.json()

    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location.get('name', place) + ", " + location.get('country', '')

    # Return ISS location information including latitude, longitude, and place name

    return {
        'latitude': lat,
        'longitude': lon,
        'place': place
    }

# =========================
# MAIN BOT LOGIC
# =========================

def main():
    print("Welcome to AstroBot\n")

    print("For Webex:", end=" ")
    token = get_webex_token()
    print("For OpenWeatherMap:", end=" ")
    weather_key = get_api_key(WEATHER_TOKEN)
    print("For API Ninjas:", end=" ")
    planet_key = get_api_key(API_NINJAS_TOKEN)

    rooms = get_rooms(token)

    if not rooms:
        print("Rooms not found!" )
        return "No rooms found. Error message: " + str(rooms)

    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    formatted_message = ""

    print("AstroBot is now running\n")

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print(f"Message: {message_text} | Message ID: {message_id}")

            if not message_text.startswith("/"):  # A command needs a prefix
                continue  # Skip if the message does not start with a prefix

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/planet <name>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith("/weather"):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:  # User did not apply a city
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1]
                    weather_today = get_weather(city, weather_key)

                    formatted_message = ""

                    if not weather_today.get("error"):
                        formatted_message = f"Weather in {weather_today['city']}, {weather_today['country']}:\n" \
                                            f"Temperature: {weather_today['temperature']}°C\n" \
                                            f"Description: {weather_today['description']}\n" \
                                            f"Humidity: {weather_today['humidity']}%\n" \
                                            f"Wind Speed: {weather_today['wind_speed']} m/s"
                    else:
                        formatted_message = weather_today['error']  # The error message

                    send_message(token, room_id, formatted_message)

            elif message_text.lower() == "/iss":

                iss_location = get_iss_location(weather_key)

                formatted_message = f"ISS is currently at:\n" \
                                    f"Latitude: {iss_location['latitude']}\n" \
                                    f"Longitude: {iss_location['longitude']}\n" \
                                    f"Place: {iss_location['place']}"

                send_message(token, room_id, formatted_message)

            elif message_text.lower().startswith("/planet"):
                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:  # If we do not have two parts, the user inputted a wrong command, so handle it by telling them the command usage
                    send_message(token, room_id, "Usage: /planet <name>")
                else:
                    planet_name = parts[1]  # Gets the planet name

                planet_info = get_planet_information(planet_name, planet_key)

                if not planet_info:
                    send_message(token, room_id, f"Error fetching planet {planet_name}")
                    continue

                formatted_message = f"Planet Information for {planet_name}:\n" \
                                    f"Mass: ~{(planet_info[0]['mass'] * (1898.13/5.9722)):.3f} Earth masses\n" \
                                    f"Radius: ~{planet_info[0]['radius'] * 11.20898073093868:.3f} Earth radii\n" \
                                    f"Orbital Period: {planet_info[0]['period']} days\n" \
                                    f"Semi-Major Axis: {planet_info[0]['semi_major_axis']} AU\n" \
                                    f"Surface Temperature: {planet_info[0]['temperature']} K ({planet_info[0]['temperature'] - 273.15:.2f}°C)\n" \
                                    f"Distance from Sun: {planet_info[0]['distance_light_year']} light-years\n" \
                                    f"Host Star Mass: {planet_info[0]['host_star_mass']} Solar masses\n" \
                                    f"Host Star Temperature: {planet_info[0]['host_star_temperature']} K ({planet_info[0]['host_star_temperature'] - 273.15:.2f}°C)"

                send_message(token, room_id, formatted_message)

            elif message_text.lower() == "/quit":
                send_message(token, room_id, "AstroBot shutting down.")
                break  # Exit the loop

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        sleep(5)  # Timeout the bot from receiving commands so that the API rate limits are limited / not exceeded too quickly

if __name__ == "__main__":
    main()
