#!/usr/bin/env python
from pprint import pprint
import requests

BASE_URL = "https://sandbox-api.brewerydb.com/v2/"  # <1>
KEY = "f884cce1da9b786cdde2ec764f736d1e"  # <2>
BREWERIES = BASE_URL + '/breweries'  # <3>

with requests.Session() as session:  # <4>
    session.params.update({'key': KEY})  # <5>
    response = session.get(BREWERIES)  # <6>
    resource_data = response.json()  # <7>
    for brewery in resource_data['data']:  # <8>
        b_name = brewery['name']
        b_id = brewery['id']
        print(f"{b_name:35} {b_id}")
