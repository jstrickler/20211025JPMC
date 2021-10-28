#!/usr/bin/env python

import bs4
import requests

response = requests.get('https://pittsburgh.craigslist.org/')
raw_html = response.text
soup = bs4.BeautifulSoup(raw_html, 'lxml')

for input_tag in soup.findAll('li', class_='s'):
    print(input_tag)
