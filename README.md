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
| Authentication Method | `Bearer Token` |
| Endpoint to list rooms | `https://webexapis.com/v1/rooms` |
| Endpoint to get messages | `https://webexapis.com/v1/messages` |
| Endpoint to send message | `https://webexapis.com/v1/messages` |
| Required headers | `Authorization: Bearer <token>` |
| Sample full GET or POST request | `_______________________________` |
---
## ISS Current Location API (2 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | `_______________________________` |
| Endpoint for current ISS location | `_______________________________` |
| Sample response format (example JSON) |
```
```
|
---
## Geocoding API (4 marks)
| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | **LocationIQ / Mapbox/ OpenWeatherMap other -provide
detail** |
| API Base URL | `http://api.openweathermap.org/geo/1.0/direct` |
| Endpoint for geocoding | `http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}` |
| Endpoint for reverse geocoding | `http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API key}` |
| Authentication method | `appid={API key}` |
| Required query parameters | `lat`, `lon`, `limit`, `appid`, `q` |
| Sample request with latitude/longitude | `51.5` |
| Sample JSON response (formatted example) |
```
```
|
---
## Weather API (3 marks)
| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | **OpenWeather, OpenWeatherMap (or other – provide
details)** |
| API Base URLs | `https://api.openweathermap.org/data/2.5/weather` |
| Endpoint for current weather | `https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API Key}` |
| Authentication method | `appId={API key}` |
| Required query parameters | `lat`, `lon`, `appId` |
| Example JSON response from https://api.openweathermap.org/data/2.5/weather?q=London |
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
|
---
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
| API Provider | '_________' |
| API Base URL | `_______________________________` |
| Endpoint | `_______________________________` |
| Authentication method | `_______________________________` |
| Required query parameters | `_______________________________` |
| Sample JSON response (formatted example) |
```
```
|
---
## Evaluation – Web Architecture, MVC Design & Security
In this section, evaluate how web technologies, architecture, and design patterns
have been applied in your **AstroBot**. Your responses must relate directly to your
implementation and include reflection on your design decisions.
---
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
- How effective is your bot in meeting the Astronomy Club’s needs?
- What design decisions worked well?
- What challenges did you face when integrating APIs?
- What security risks did you identify and how were they handled?
- How could your solution be improved in the future?
---
**Tip:** Link your answers directly to your code and examples for higher marks.
### References
- developer.webex.com (2026). REST API Basics. Available at: https://developer.webex.com/docs/rest-api-basics [Accessed 30 Sept. 2026]
- openweathermap. (2026). One call API 4.0. Openweathermap.Org. https://openweathermap.org/api/one-call-4?collection=one_call_api [Accessed 30 Sept. 2026]
- Reitz, K. (2026). Getting Started with Requests. Requests.Readthedocs.Io. https://requests.readthedocs.io/en/latest/user/quickstart/ [Accessed 25 Sept. 2026]
w3schools. (2023). Python requests module. Www.W3schools.Com. https://www.w3schools.com/python/module_requests.asp [Accessed 25 Sept. 2026]
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---
### Total: /40