#!/usr/bin/python3
'''Shar'''

import urllib.request
import json
import pprint

GLOBALVAR1 = 'http://api.open-notify.org/astros.json'

def main():
    '''reading json from api'''
    # call the api
    groundctrl = urllib.request.urlopen(GLOBALVAR1)
    groundctrl_output = groundctrl.read()
    print(groundctrl_output)
    ground = json.loads(groundctrl_output.decode('utf-8'))
    print(ground)

    print(ground["number"])
    print(type(ground["people"][0]))

    for astro in ground["people"]:
        print(astro["name"])
        

    for astro in ground["people"]:
        print(astro["craft"])


if __name__ == "__main__":
    main()
