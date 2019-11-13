#!/usr/bin/env python3
import requests
import json

GETURL = "http://validate.jsontest.com/"

def main():
   
    mydata = {"fruit" : ["apple","pear"], "vegetable" : ["carrot"]}
#    jsontovalidate = "?json" + str(mydata).replace(" ","")
#    jsontovalidate = f"json={ str(mydata).replace(' ','') }"
#    jsontovalidate = f"?json={mydata.replace(' ', '')}
    jsontovalidate = f"json={ json.dumps(mydata).replace(' ', '') }"
    print(jsontovalidate)
    resp = requests.get(f"{GETURL}?{jsontovalidate}")
    
    respjson = resp.json()
    print(respjson)


if __name__ == "__main__":
    main()
