#!/usr/bin/env python3
import requests
import argparse
import pandas

POKEURL = "http://pokeapi.co/api/v2/item"

def main():
    items = requests.get(f"{POKEURL}?limit=1000").json()

    list1 = []

    for item in items.get("results"):
       # if 'heal' in item.get("name")
        if args.searchword in item.get("name"):
            list1.append(item.get("name"))

    print(f"There are {len(list1)} : {list1}")

    ## export to excel with pandas
    # make a dataframe from our data
    itemsDF = pandas.DataFrame(list1)
    itemsDF.to_excel("pokemonitems.xlsx", index=False) # export to MS Excel format --> requires openpyxl
    itemsDF.to_csv("pokemonitems.csv", index=False) # export to CSV format; index=False or orient='records' (for json) makes sure the line doesn't contain index numbers
    itemsDF.to_json("pokemonitems.json", orient='records')
    print("Goota catch em' all")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search")
    parser.add_argument('searchword', metavar='SEARCHWORD', type=str,default='ball',help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()
