#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

SITE = 'http://www.pitankar.com/'

def getSite(url):
    r = requests.get(url)

    if r.status_code is not 200:
        print ("The site returned status code {}".format(r.status_code))

    return r.text

if __name__ == '__main__':
    site = BeautifulSoup(getSite(SITE), 'html.parser')
    a = site.find_all('h2', {'class':'post-title'})

    f = open('data.csv', 'w')
    for i in a:
        site = BeautifulSoup(getSite(i.a.attrs['href']), 'html.parser')
        post_title = site.find('h1', {'class':'post-title'})
        date = site.find('li', {"class":"post-date"})
        catagory = site.find('a', {"rel":"category tag"})
        f.write(post_title.text + ', ' + date.text + ', ' + catagory.text + '\n')
    f.close()