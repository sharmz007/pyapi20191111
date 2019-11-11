#!/usr/bin/env python3
  
import requests

GLOBALVAR2 = 'http://api.open-notify.org/astros.json'

def main():
    x = requests.get(GLOBALVAR2)
    y = x.json()

    print(type(y))
    for astro in y["people"]:
        print(astro["name"])

if __name__ == "__main__":
    main()
