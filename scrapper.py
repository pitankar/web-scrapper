#!/usr/bin/python3

import requests
import bs4

SITE = 'http://www.pitankar.com/'

def getSite(url):
    r = requests.get(url)

    if r.status_code is not 200:
        print ("The site returned status code {}".format(r.status_code))

    return r.text

if __name__ == '__main__':
    getSite(SITE)