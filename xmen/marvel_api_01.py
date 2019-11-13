#!/usr/bin/python3
import argparse
import time
import hashlib

import requests

XAVIER = 'http://gateway.marvel.com/v1/public/characters'

def hashbuilder(time,privkey,pubkey):
    #hashlib will give a decimal number; hexdigest will output a HEX value
    return hashlib.md5((time,privkey,pubkey).encode('utf-8')).hexdigest()

def marvelcharcall(time,hashval,privkey,pubkey,lookupname):
    resp = requests.get(f"{XAVIER}?name={lookupname}&ts={time}&apikey={pubkey}&hash={hashval}")
    return resp.json()

def main():
    ## harvest private key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')

    ## create an integer from a float timestamp (for our RAND)
    nightcrawler = str(time.time()).rstrip('.')

    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    cerebro = hashbuilder(nightcrawler, beast, storm)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, "Wolverine")

    ## display results
    print(uncannyxmen)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    parser.add_argument('--name', help='Provide the Marvel character name')
    args = parser.parse_args()
    main()
