import requests
import json
from datetime import datetime
import time

# =========================
# CONFIGURATION FUNCTIONS
# =========================

BASE_WEBEX_URL = "https://webexapis.com/v1/"
BASE_OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/weather"
BASE_GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_REVERSE_GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/reverse"
BASE_ISS_URL = "http://api.open-notify.org/iss-now.json"

# These tokens will be reset and removed in the final public release version.
# If you found this previous version and tried to use it, nice try, it won't work.
WEBEX_TOKEN = "Bearer ZGNjNTAzMTctZTVmNS00ZTExLWI3M2YtN2I3MzdhMTFlNTAxN2JlMThjMzQtNTEx_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17"
WEATHER_TOKEN = "1f97fe4a84b771c9268dce4e8a3f3ab2"  # OpenWeatherMap API Key

def get_webex_token():  # Asks the user for a Webex token or uses a hardcoded one
    
    return WEBEX_TOKEN  # This line will be omitted in public version
    choice = input("Use hard-coded Webex token? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ")
        return f"Bearer {token}"
    else:  # Hardcoded token
        return "Bearer MY_WEBEX_TOKEN"
    
def get_api_key(hardcoded_key):
    #complete the function to get the API key from user input or use a hardcoded key
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
    headers = {'Authorization': token}  #complete the headers dictionary to include the Authorization header with the token
    response = requests.get(url, headers=headers)  #complete the request to get rooms using requests.get with the url and headers

    if response.status_code != 200:  #complete the condition to check if the response status code is not 200:
        print("Error fetching rooms. ERROR CODE", response.status_code)
        return None

    return response.json().get("items", None)  # Attempts to get "items" from JSON response. Returns empty list if not found.

def print_rooms(rooms):
    print(rooms)
    for room in rooms:
        print(f"Room Name: {room['title']} | ID: {room['id']}")

def select_room(rooms):
    while True:
        name = input("Enter the room name you wish to select: ")
        for room in rooms:
            if name.lower() in room["title"].lower():
                print(f"Selected Room: {room['title']}")
                return room["id"]
        print("Room not found!")

def get_latest_message(token, room_id):
    url = BASE_WEBEX_URL+"messages"  #  https://webexapis.com/v1/messages
    params = {'roomId': room_id, 'max': '20'}  # Use 'roomId' and 'max' parameter to fetch the room and limit the number of messages returned to 20
    headers = {'Authorization': token}  # Use auth token in headers with our request

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Error fetching messages. ERROR CODE", response.status_code)
        return None, None

    data = response.json().get("items", [])

    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")

def send_message(token, room_id, message):
    url = BASE_WEBEX_URL+"messages"
    headers = {'Authorization': token, 'Content-Type': 'application/json'} #complete the headers dictionary to include the Authorization header with the token and Content-Type as application/json
    data = {
        "roomId": room_id,
        "text": message
    }
    requests.post(url, headers=headers, data=json.dumps(data))

# =========================
# WEATHER FUNCTIONS
# =========================

def get_city_coordinates(city, api_key):
    params = {'q': city, 'limit': 1, 'appid': api_key}  # city name, limit, and the API key in params
    response = requests.get(BASE_GEOCODING_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if location is None:
        print("No location found!")
        return {'error': 'No city data found'}  # if .get() fails, return an error message as a fallback

    params = {'lat': location['lat'], 'lon': location['lon'], 'units': 'metric', 'appid': api_key}  # latitude, longitude, units as metric, and the API key

    response = requests.get(BASE_OPENWEATHERMAP_URL, params=params)

    if response.status_code != 200:  # The response was unsuccessful
        print("No weather info found, status code error:", response.status_code)
        return {'error': 'No weather data found'}  # if .get() fails, return an error message as a fallback

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
        return {'error': 'No ISS location data found'}  # if .get() fails, return an error message as a fallback

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
    print("Running AstroBot")
    #token = get_api_key(get_webex_token())
    #rooms = get_rooms(token)
    #print_rooms(rooms)
    #print(get_iss_location(WEATHER_TOKEN))

if __name__ == "__main__":
    main()
