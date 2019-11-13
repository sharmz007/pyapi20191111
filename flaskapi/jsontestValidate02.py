#!/usr/bin/env python3
import requests
import json

POSTURL = "http://validate.jsontest.com/"

def main():
   
    mydata = {'json' : "{'fruit' : ['apple','pear'], 'vegetable' : ['carrot']}"}
#    jsontovalidate = "?json" + str(mydata).replace(" ","")
#    jsontovalidate = f"json={ str(mydata).replace(' ','') }"
#    jsontovalidate = f"?json={mydata.replace(' ', '')}
#    jsontovalidate = f"json={ json.dumps(mydata).replace(' ', '') }"
#    print(jsontovalidate)
    resp = requests.post(POSTURL, data=mydata)
    respjson = resp.json()
    print(respjson)


if __name__ == "__main__":
    main()
