import requests
import json
from datetime import datetime
import time

# =========================
# CONFIGURATION FUNCTIONS
# =========================

WEBEX_URL = "https://webexapis.com/v1/"

def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ")
        return f"Bearer {token}"
    else:
        return "Bearer MY_WEBEX_TOKEN"
    
def get_api_key(prompt, hardcoded_key):
    #complete the function to get the API key from user input or use a hardcoded key
    choice = input(prompt).lower()
    if choice == "n":
        return input("Enter your API Key: ")
    else:
        return hardcoded_key
  
def main():
    print("Running AstroBot")

    # simple test
    print(get_webex_token())
    print(get_api_key("Use hard-coded API key? (y/n):", "TEST"))

print(main())

# =========================
# WEBEX FUNCTIONS
# =========================