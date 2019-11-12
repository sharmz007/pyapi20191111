#!/usr/bin/env python3

import requests
import pprint

# test API's from https://www.anapioficeandfire.com/api

AOIF = "https://www.anapioficeandfire.com/api"
AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    gotresp = requests.get(AOIF)
    
    gotdecodejson = gotresp.json()
#    print(gotdecodejson)

    gotbooks = (requests.get(AOIF_BOOKS)).json()
    print()
    for book in gotbooks:
        print(book["name"] + " has a total of ",book["numberOfPages"], " pages")
        print("The isbn number is ",book["isbn"])
        print("The publisher number is ",book["publisher"])
        print("The number of characters are ",len(book["characters"]))
        print()
#        print(book["characters"].len())

#        print("{}, pages - {}".format(singlebook["name"], singlebook["numberOfPages"]))
#        print(f'{singlebook["name"]}, pages = {singlebook["numberOfPages"]'})
        #pprint.pprint(name)


if __name__ == "__main__":
    main()
