#!/usr/bin/env python3
import requests
#import urllib.request
import json

jsonhttp = "http://"
jsonTestDomain = "jsontest.com"

def gettime():
    try:
        timenow = (requests.get(f"{jsonhttp}date.{jsonTestDomain}")).json 
#        timenow = (requests.get(f"{jsonhttp}date.{jsonTestDomain}"))
        if timenow.status != 503:
           print(f"The time now is {timenow}") 
        #else:
         #   print(f"The time is now {timenow}")
    except Exception as error:
        print(f"Oops error.  Something went wrong'{error}")
        
#    print(f"The time now is {timenow}")
#    return timenow['date']
#    pass


def getmyIP():
#    myIP = (requests.get(f"{jsonhttp}ip.{jsonTestDomain}")).json()
    try:
        myip = (requests.get(f"{jsonhttp}ip.{jsonTestDomain}")).json 
        if myip.status != 503:
           print(f"My IP address is {myip}")
    except Exception as error:
        print(f"Something went wrong'{error}")
#    return myIP['ip']
#    pass

def servers():
    with open("/home/student/pyapi/flaskapi/myservers.txt", "r") as servers:
       myservers = (servers.readlines())
    serverlist = [server.strip() for server in myservers]
    return serverlist
    
def main():
#    print('The time now is',gettime())
#    print('My IP address is',getmyIP())
#    print('My servers are ',servers())
    servers()
    getmyIP()
    gettime()
    print()

if __name__ == "__main__":
    main()

