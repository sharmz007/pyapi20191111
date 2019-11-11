#!/usr/bin/env python3

import requests
import pprint

API = "https://api.nasa.gov/planetary/apod?"
API_KEY = "api_key="

def main():
    with open("/home/student/creds", "r") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = nasacreds.strip("\n")
#    print(nasacreds)
    
    apodresponse = requests.get(API + API_KEY + nasacreds)

    apod = apodresponse.json()

    print(type(apod))
    print("\nTitle " + apod["title"] + "\n")
    print("Date: " + apod["date"] + "\n")
    print("Explanation: " + apod["explanation"] + "\n")
    print("URL: " + apod["url"] + "\n")

#    pprint.pprint(apod)
#    pprint.pprint(apod["explanation"])

if __name__ == "__main__":
    main()
