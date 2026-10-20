# 🚀 Space Bot API Investigation Sheet
## Webex Messaging API
| Criteria | Details |
|---------|---------|
| API Base URL | `https://webexapis.com/v1/` |
| Authentication Method | `Bearer TOKEN` |
| Endpoint to list rooms | `GET /rooms` |
| Endpoint to get messages | `GET /messages` |
| Endpoint to send message | `POST /messages` |
| Required headers | `Authorization: Bearer <token>` |
| Sample full GET or POST request | `GET https://webexapis.com/v1/rooms` |
---
## ISS Current Location API
| Criteria | Details |
|---------|---------|
| API Base URL | `http://api.open-notify.org` |
| Endpoint for current ISS location | `/iss-now.json` |
### Sample Response Example
```json
{
  "message": "success",
  "timestamp": 1791361847,
  "iss_position": {
    "longitude": "36.3186",
    "latitude": "50.8223"
  }
}
```

## Geocoding API
| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | **LocationIQ / Mapbox/ OpenWeatherMap other - provide detail** |
| API Base URL | `http://api.openweathermap.org/geo/1.0/direct` |
| Endpoint for geocoding | `/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}` |
| Endpoint for reverse geocoding | `/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API key}` |
| Authentication method | `appid={API key}` |
| Required query parameters | `lat`, `lon`, `limit`, `appid`, `q` |
| Sample request with latitude/longitude | `http://api.openweathermap.org/geo/1.0/reverse?lat=51.5074456&lon=-0.1277653&limit=1&appid={API key}` |
### Forward Geocoding Example
```json
[
    {
        "name": "London",
        "local_names": {
            "br": "Londrez",
            "to": "Lonitoni",
            "vi": "Luân Đôn",
            "kk": "Лондон",
            "ab": "Лондан",
            "or": "ଲଣ୍ଡନ",
            "ca": "Londres",
            "ja": "ロンドン",
            "pl": "Londyn",
            "km": "ឡុងដ៍",
            "ht": "Lonn",
            "om": "Landan",
            ...  // There was much more but I truncated it here 
        },
        "lat": 51.5074456,
        "lon": -0.1277653,
        "country": "GB",
        "state": "England"
    }
]
```
### Reverse Geocoding Example
```json
[
    {
        "name": "City of Westminster",
        "local_names": {
            "be": "Вэстмінстэр",
            "he": "וסטמינסטר",
            "bn": "সিটি অফ ওয়েস্টমিনস্টার",
            "hi": "सिटी ऑफ वेस्टमिंस्टर",
            "fr": "Cité de Westminster",
            "ru": "Вестминстер",
            "cy": "San Steffan",
            "en": "City of Westminster",
            "sr": "Вестминстер",
            "ko": "시티오브웨스트민스터",
            "mk": "Град Вестминстер"
        },
        "lat": 51.4973206,
        "lon": -0.137149,
        "country": "GB",
        "state": "England"
    }
]
```
---
## Weather API
| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | OpenWeatherMap |
| API Base URLs | `https://api.openweathermap.org/data/2.5/weather` |
| Endpoint for current weather | `/data/2.5/weather?q={city}&units=metric&appid={API Key}` |
| Authentication method | `appId={API key}` |
| Required query parameters | `lat`, `lon`, `appId` |
### Example JSON Response
Using: https://api.openweathermap.org/data/2.5/weather?q=London
```json
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "broken clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 21.09,
    "feels_like": 21.42,
    "temp_min": 20.27,
    "temp_max": 22.25,
    "pressure": 1012,
    "humidity": 83,
    "sea_level": 1012,
    "grnd_level": 1009
  },
  "visibility": 10000,
  "wind": {
    "speed": 6.7,
    "deg": 202,
    "gust": 9.2
  },
  "clouds": {
    "all": 70
  },
  "dt": 1790764617,
  "sys": {
    "type": 2,
    "id": 2075535,
    "country": "GB",
    "sunrise": 1790747944,
    "sunset": 1790790114
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
```

## Epoch to Human Time Conversion

| Criteria | Details |
|---------|---------|
| Library used | `datetime` |
| Function used to convert epoch (Bijay Kumar, 2025) | `datetime.fromtimestamp()` |
| Sample code to convert timestamp |
```py
from datetime import datetime

epoch_time = 1234567890

print(datetime.fromtimestamp(epoch_time))
```
Output (human-readable time): `2009-02-13 23:31:30`

---
## Extended Feature API
| Criteria | Details |
|---------|---------|
| API Provider | 'API Ninjas' |
| API Base URL | `https://api.api-ninjas.com/v1/planets` |
| Endpoint | `/v1/planets` |
| Authentication method | `X-Api-Key: API_KEY` |
| Required query parameters | `name` |
### Sample JSON response (formatted example)
```json
[
  {
    "name": "Mars",
    "mass": 0.000338,
    "radius": 0.0488,
    "period": 687.0,
    "semi_major_axis": 1.542,
    "temperature": 210.0,
    "distance_light_year": 3.7e-05,
    "host_star_mass": 1.0,
    "host_star_temperature": 6000.0
  }
]
```

## Evaluation – Web Architecture, MVC Design & Security
Evaluating how web technologies, architecture, and design patterns that have been applied in AstroBot.
### Web Architecture – Client–Server Model
How the client interacts with the server through sending messages and getting responses.
- The user (client) interacts with AstroBot through sending it commands on Webex.
- Webex is the main server, handling the User Interface (UI) and messaging platform my bot runs on. The APIs are services used to send and retrieve data.  This includes Webex for sending and retrieving messages, OpenWeatherMap for forward and reverse geocoding, and weather information, Open Notify for ISS location, and API Ninjas for planetary information.

#### Example
A user sends a commant which is received by the server is captured by AstroBot using a GET request with the Webex API. The user data is processed and connected to the relevant API, which is sent and retrieved. The request of the specific API is processed and formatted for the user, before being sent back to them with a POST request using the Webex API for the client to see.
#### Security Considerations
- Processing data could expose API keys within the log, so data is handled safely without leaving traces of sensitive information. Logging should only contain relevant information to the developer or anyone who has access without exposing sensitive information. Using `getpass()` allows API keys and tokens being pasted manually are not logged, making them invisible. Additionally, a `.env` file would store these authentication keys allowing for a faster login without exposing what the keys are in the console.
- Inputs are validated so errors are handled properly. By having specific matching patterns by using `if`, `elif`, and `else` with messages matching `/`, we can control what commands are valid and should be used. The `else` block handles any invalid commands, redirecting the user to use the `/help` command if they are stuck. If a command is correctly formatted but has wrong parameters, it should be also handled, returning an invalid command message. Example: `/planet Krypton` -> `Error fetching planet Krypton`.
---
### RESTful API Usage in Your Application
REST, standing for REpresentational State Transfer. This allows programs to transfer resources between components. (Gupta, L., 2019).
#### HTTP Method Usage
- Using `requests.get()`, you can retrieve data from a specified url, and can pass data with it to get a response. In my program, I used Webex url with `/messages` and `/rooms` to get information about what the user sent and what room to look for those messages in. For example, in `/messages`I use `requests.get(url, headers=headers, params=params)` to get their response, attaching my authorization token and any parameters like `roomId` to retrieve the relevant response.
- Using `requests.post()`, you can send data. I use it to post messages back to the user after retrieving relevant data based on the command they ran. For example, a user sends the command `/iss`. After retrieving and formatting data like converting the coordinates to see if it is flying over a specific city, that information is posted back to the user so they can see it visually in a more human-readable format. I use `requests.post(url, headers=headers, data=json.dumps(data))` to do this.
#### API Interaction Examples
- `/city London` will give relevant weather data in London, such as temperature and forecast description.
- `/planet Mars` gives planetary information about Mars, such as mass, orbital period, and radius, which are converted in terms of Earth ratio.
### JSON Responses Processing

#### Data Retrieval and Processing 
APIs return data in the format of JSON, which is processed using `.json()` so that python can read it properly. JSON has headings which can be retrieved through specifying the name of the data you wish to use.
#### Example using `/weather London`
After recieving the command, we first match if the user message starts with `/weather` to ensure it is the command we want to process. We do this using `message_text.lower().startswith("/weather")`. Next, we split the message into parts using `parts = message_text.split(maxsplit=1)` and make sure there are two parts; the `/weather` and `London`. Now we can use `London` as a query parameter to get weather information using our `OpenWeatherMap` API url. Convert any data which was a bad request gracefully to readable information, and use `weather['TITLE']` to get the information we need. Example: `weather['temperature']` returns the temperature of the weather in London.
#### Code Example
```py
def get_city_coordinates(city, api_key):
    params = {'q': city, 'limit': 1, 'appid': api_key}  # city name, limit, and the API key in params
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=params)

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

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

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
```

#### Security Considerations
Checking and handling status codes is used to prevent the bot from crashing, acting as a failsafe. When a status code recieved from an API `GET` request. If the status returned is `200`, the request was successful and worked as expected (Jain, P., 2025). If there was any other status code returned, we can return information not found, or None. For example, if `/weather London` was not a success, a message of  "weather information not found" or "City was not found".

Calling APIs can result in a rate limit if we reach a specific number of calls, so data could be cached locally for a limited time. For example, if the Astronomy Club frequently ran the command `/weather London`, the API could put us on timeout. The solution would be to cache the result once, then return the cached result every time the user calls `/weather London`. With weather for example,, it is unlikely that a forecast changes quickly, so say during 2 minutes we return the cached result, and when the timer ends, we call the OpenWeatherMap API again and repeat the process.

---
### MVC Design Pattern in AstroBot

| Component | Description (geeksforgeeks, 2025) | Example |
|------------|----------------------------------|------|
| **Model** | Data logic the user works with | API interaction data - Weather function requests for weather related data from OpenWeatherMap |
| **View** | Information displayed visually to the user | Formatted response of the weather in London; temperature, wind speed, forecast description, etc.. |
| **Controller** | Link between the Model and the View, what actions the Model should to take | User sends `/planet Mars`, Mars is identified by the bot, extracts it, and calls the `get_planet_information()` function with `Mars`. Data is processed, formatted, and send back to the user as a message |
---
### 🚀 Reflection and Evaluation

AstroBot is effective at completing its task. It gives the Astronomy Club relevant information through simple commands without the users needing to search on the web. `/weather <city>` retrieves weather information such as the forecast, and `/iss` for information displaying the ISS's latitude and longitude. This enables the Astronomy Club to plan observations of the night sky or International Space Station (ISS) more effectively by running one command to get the needed information. `/planet <name>` gives statistics about a planet, like its mass (in Earth masses), surface temperature (in both Kelvin and Celsius), and other information. This will help members learn more about different planets and engage them in discussion.

One design that worked well was to use slash commands. Starting with a `/`, it becomes easy to understand what a command looks like, and is user friendly to both new and experienced members of the club. `/help` provides a list of all commands available, showing a simplistic way to use them. Not only can this be helpful for new users showing them how to use commands, but also for experienced users to display any new commands that could be added in the future. In my code, modularizing functions such as `get_weather()` and `get_iss_location()` allows for better maintainability, testing, and troubleshooting. The formatted errors and responses further contribute to improving user and developer experience, as they would understand outputted results and issues better.

When intergrating APIs, I found that formatting received JSON responses was challenging, as there was lots of data format, which needed multiple validation tests to verify it was correct. Converting planet data mass in relation to Earth mass was difficult, but using official NASA web pages I was able to use the conversion value.

API access tokens in my source code is a clear security risk. To keep myself safe from my API keys being stolen, I have removed them from the code, especially for the public release, and stored in a `.env` file. Users can also input their API tokens manually if they wish not to store them. Sensitive information such as API keys are never printed or logged.

For future improvements:
- Predict where the ISS will be given a date and time
- Predicted weather forecast for a location, date, and time

This allows the Astronomy club to plan further in advance when observing the ISS, or looking for a clear day/night to observe stars or planets. It would also help the club decide which days to perform these observations. If a day/night is known to be rainy or have thunder, they can reschedule their event and avoid unnecessary trips.

---
### References
- API Ninjas (2019). Planets API. API Ninjas. Available at: https://api-ninjas.com/api/planets [Accessed 14 Oct. 2026].
- developer.webex.com (2026). REST API Basics. Available at: https://developer.webex.com/docs/rest-api-basics [Accessed 30 Sept. 2026]
- GeeksforGeeks (2017). Getpass() and getuser() in python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/getpass-and-getuser-in-python-password-without-echo/ [Accessed 20 Oct. 2026].
- GeeksforGeeks (2025). MVC framework introduction.GeeksforGeeks. Available at: https://www.geeksforgeeks.org/software-engineering/mvc-framework-introduction/ [Accessed 14 Oct. 2026].
- Gupta, L. (2019). What is REST – learn to create timeless REST APIs. Restfulapi.net. Available at: https://restfulapi.net/ [Accessed 19 Oct. 2026].
- Jain, P. (2025). HTTP STATUS CODES: Complete list & troubleshooting guide. Bluehost Blog. Available at: https://www.bluehost.com/blog/http-status-codes/ [Accessed 20 Oct. 2026].
- Kumar, B. (2025). Epoch time to datetime conversion in python. Python Guides. Available at: https://pythonguides.com/python-epoch-to-datetime/ [Accessed 14 Oct. 2026].
- NASA (2018). Jupiter fact sheet. Nasa.gov. Available at: https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html [Accessed 14 Oct. 2026].
- Open-notify.org. (2025). Open Notify API Documentation. Available at: http://open-notify.org/Open-Notify-API/ [Accessed 7 Oct. 2026].
- openweathermap. (2026). One call API 4.0. Openweathermap.Org. https://openweathermap.org/api/one-call-4?collection=one_call_api [Accessed 30 Sept. 2026]
- Reitz, K. (2026). Getting Started with Requests. Requests.Readthedocs.Io. https://requests.readthedocs.io/en/latest/user/quickstart/ [Accessed 25 Sept. 2026]
- w3schools. (2023). Python requests module. Www.W3schools.Com. https://www.w3schools.com/python/module_requests.asp [Accessed 25 Sept. 2026]