import requests
import json
from datetime import datetime
import time

# =========================
# CONFIGURATION FUNCTIONS
# =========================

BASE_WEBEX_URL = "https://webexapis.com/v1/"  # Base Webex URL

def get_webex_token():  # Asks the user for a Webex token or uses a hardcoded one
    # Yes, this main token will be removed in the final version.
    # If you found this previous version and tried to use it, nice try, it won't work.
    return "Bearer ZGNjNTAzMTctZTVmNS00ZTExLWI3M2YtN2I3MzdhMTFlNTAxN2JlMThjMzQtNTEx_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17"
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
    url = BASE_WEBEX_URL+"rooms"  # URL to fetch rooms from Webex API
    headers = {"Authorization": token}  #complete the headers dictionary to include the Authorization header with the token
    response = requests.get(url, headers=headers)  #complete the request to get rooms using requests.get with the url and headers

    if response.status_code != 200:  #complete the condition to check if the response status code is not 200:
        print("Error fetching rooms. ERROR CODE", response.status_code)
        return []

    return response.json().get("items", [])  # Attempts to get "items" from JSON response. Returns empty list if not found.


def print_rooms(rooms):
    print(rooms)
    for room in rooms:
        print(f"Room Name: {room}")

def get_latest_message(token, room_id):
    url = BASE_WEBEX_URL+"messages"  #complete the URL to fetch messages from Webex API
    params = {"roomId": room_id, "max": "20"}
    headers = {"Authorization": token}  #complete the headers dictionary to include the Authorization header with the token

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Error fetching messages. ERROR CODE", response.status_code)
        return None, None

    data = response.json().get("items", [])

    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")


# =========================
# MAIN BOT LOGIC
# =========================
def main():
    print("Running AstroBot")
    rooms = get_rooms(get_api_key(get_webex_token()))
    print_rooms(rooms)

if __name__ == "__main__":  # 
    print(main())

# =========================
# WEBEX FUNCTIONS
# =========================