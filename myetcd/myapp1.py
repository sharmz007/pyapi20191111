#!/usr/bin/env python3
import requests
import json
from colorama import Fore, Style


URL = "http://127.0.0.1:2379/v2/keys/tickets"

def getalltickets():
    ## GET request on a directory
    print("\n\nRetrieving all ticket. Please wait\n\n")
    tickets = requests.get(URL).json()
#    print(type(tickets))
    ticketlist = tickets["node"]["nodes"] ##this is the same as tickets.get("node").get("nodes")
#    for ticket in ticketlist:
#        print(f'Ticket ID: {ticket["key"]}'.lstrip("/tickets/"))
#    print(f'\n{tickets["node"]["nodes"][0]["key"]}'.strip("tickets"))
#    pass
    return ticketlist

def getticket(ticketnumber):
    tickets = requests.get(URL).json()
    index = int(ticketnumber) - 1
    for ticket in tickets:
        if ticketnumber == ticket.get("key").lstrip("/tickets/"):
           descr = tickets.get("value")  
           #print(descr)
    ## GET request
    return descr

def createticket():
    ## POST request
    pass

def updateticket():
    ## PUT request
    pass

def deleteticket():
    ## DELETE request
    pass

def main():
    while True:
        option = input('''
        What would you like to do?
              1) read tickets
              2) get ticket
              3) create ticket
              4) update ticket
              5) delete ticket "This will wipe out everything"
              6) Exit

        Choose an option: ''')
        
        if option == "1": 
            tickets = []
            ticketlist = getalltickets()
            for ticket in ticketlist:
                ticketID = ticket["key"]#.lstrip("/tickets/")
                value = ticket["value"]
                tickets.append(ticketID)
                print(f'{ticketlist.index(ticket)+1}) Ticket ID: {ticketID.lstrip("/tickets/")}     Description: {value}')
           #     print(f'Ticket ID: {ticket["key"]}'.lstrip("/tickets/"))
           #    print(f'\n{tickets["node"]["nodes"][0]["key"]}'.strip("tickets")
            option = input("\n\nWould you like to continue? (Yes/No): ")
            if option == "Yes": ## or  "Y" or "yes" or "y"
               pass
            else:
               print("\n\nYou are exiting the app now\n\n")
               break
        elif option == "2":
#            printtickets()
            whichticket = input("\n\nSelect the list number for the ticket i.e. 1) : ")
            print(f"\n\nHere is the description for the ticket ===> {Fore.GREEN}'{getticket(whichticket)}'{Style.RESET_ALL}")
        elif option == "6":
            print("\n\nYou are exiting the app now\n\n")
            break
        else:
            print("\n\n\n ^^^^ Please enter a valid option\n\n")
#        print("The app is running")

if __name__ == "__main__":
    getalltickets()
    main()
