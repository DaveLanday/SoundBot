#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#scrape_sound.py
#Dave Landay
#LAST UPDATED: 03-26-2020

from bs4 import BeautifulSoup
import requests

url = 'https://www.soundboard.com/'
page = requests.get(url)
print('page stats: ', page.status_code)
scraper = BeautifulSoup(page.text, 'html.parser')
print(scraper.prettify())

