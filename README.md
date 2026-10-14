# 🚀 Space Bot API Investigation Sheet
**Total Marks: 40**
**TASK 1: Collect Required API Documentation**
This investigation sheet helps you gather key technical information from the three
APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current
Location API**, **Weather API** and a **Geocoding API** , plus the Python time
module. Also furhter investigate the application of Web Architecture and MVC design
pattern in development of the Bot
---
## Webex Messaging API (4 marks)
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
## ISS Current Location API (2 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `http://api.open-notify.org` |
| Endpoint for current ISS location | `/iss-now.json` |
### Sample response format (example JSON)
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

## Geocoding API (4 marks)
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
## Weather API (3 marks)
| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | OpenWeatherMap |
| API Base URLs | `https://api.openweathermap.org/data/2.5/weather` |
| Endpoint for current weather | `/data/2.5/weather?q={city}&units=metric&appid={API Key}` |
| Authentication method | `appId={API key}` |
| Required query parameters | `lat`, `lon`, `appId` |
### Example JSON response from https://api.openweathermap.org/data/2.5/weather?q=London
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

## Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |
```
```
|
| Output (human-readable time) | `_______________________________` |
---
## Extended Feature API ( 3 marks)
| Criteria | Details |
|---------|---------|
| API Provider | 'API Ninjas' |
| API Base URL | `https://api.api-ninjas.com/v1/planets` |
| Endpoint | `/v1/planets` |
| Authentication method | `X-Api-Key: API_KEY` |
| Required query parameters | `name` |
### Sample JSON response (formatted example)
```jsonl
[{
    'name': 'Mars',
    'mass': 0.000338,
    'radius': 0.0488,
    'period': 687.0,
    'semi_major_axis': 1.542,
    'temperature': 210.0,
    'distance_light_year': 3.7e-05,
    'host_star_mass': 1.0,
    'host_star_temperature': 6000.
}]
```

## Evaluation – Web Architecture, MVC Design & Security
In this section, evaluate how web technologies, architecture, and design patterns
have been applied in your **AstroBot**. Your responses must relate directly to your
implementation and include reflection on your design decisions.

### Web Architecture – Client–Server Model (3 marks)
Explain how the client–server model applies to your AstroBot:
- Identify the **client**
- Identify the **server(s)**
- Describe how data flows between:
- User, AstroBot and APIs
Include a **simple block diagram** to illustrate this interaction.
#### Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate
limiting, and Input validation (e.g., handling user commands safely), include
examples from code where necessary to illustrate.
---
### RESTful API Usage in Your Application (3 marks )
Explain how REST APIs are used in your AstroBot:
- Describe how HTTP methods (GET, POST) are used
- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)
- Describe how JSON responses are received and processed
Note: Relate your explanation directly to your code for higher grade.
#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses,
Avoiding excessive API calls
---
### MVC Design Pattern in AstroBot (3 Marks)
Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation
| Component | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model** | |
| **View** | |
| **Controller** | |
---
### 🚀 Reflection and Evaluation ( 8 marks )
Reflect on your AstroBot (400 words):
AstroBot is effective at completing its task. It gives the Astronomy Club relevant information through simple commands without the users needing to search on the web. `/weather <city>` retrieves weather information such as the forecast, and `/iss` for information displaying the ISS's latitude and longitude. This enables the Astronomy Club to plan observations of the night sky or International Space Station (ISS) more effectively by running a simple command to get this information quickly. `/planet <name>` gives statistics about a planet, like its mass (in Earth masses), surface temperature (in both Kelvin and Celsius), and distance from the sun in light years. This is useful for astronomy discussions, which helps members learn more about different planets.

One design that worked well was to use slash commands. Starting with a `/`, it becomes easy to understand what a command looks like, and is user friendly to both new and experienced members of the club. `/help` provides a list of all commands available, showing a simplistic way to use them. Not only can this be helpful for new users showing them how to use commands, but also for experienced users to display any new commands that could be added in the future.

- ~~How effective is your bot in meeting the Astronomy Club’s needs?~~  
- ~~What design decisions worked well?~~
- What challenges did you face when integrating APIs?
- What security risks did you identify and how were they handled?
- How could your solution be improved in the future?
---
**Tip:** Link your answers directly to your code and examples for higher marks.
### References
- API Ninjas (2019). Planets API. API Ninjas. Available at: https://api-ninjas.com/api/planets [Accessed 14 Oct. 2026].
- developer.webex.com (2026). REST API Basics. Available at: https://developer.webex.com/docs/rest-api-basics [Accessed 30 Sept. 2026]
- Open-notify.org. (2025). Open Notify API Documentation. Available at: http://open-notify.org/Open-Notify-API/ [Accessed 7 Oct. 2026].
- openweathermap. (2026). One call API 4.0. Openweathermap.Org. https://openweathermap.org/api/one-call-4?collection=one_call_api [Accessed 30 Sept. 2026]
- Reitz, K. (2026). Getting Started with Requests. Requests.Readthedocs.Io. https://requests.readthedocs.io/en/latest/user/quickstart/ [Accessed 25 Sept. 2026]
w3schools. (2023). Python requests module. Www.W3schools.Com. https://www.w3schools.com/python/module_requests.asp [Accessed 25 Sept. 2026]

- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.

---
### Total: /40