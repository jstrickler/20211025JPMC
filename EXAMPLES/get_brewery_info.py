#!/usr/bin/env python
from pprint import pprint
import requests

BASE_URL = "https://sandbox-api.brewerydb.com/v2/"  # <1>
KEY = "f884cce1da9b786cdde2ec764f736d1e"  # <2>
BREWERY = BASE_URL + '/brewery/'  # <3>
BREWERY_IDS = ["BznahA", "nLsoQ9", "AqEUBQ"]  # <4>

with requests.Session() as session:  # <5>
    session.params.update({'key': KEY})  # <6>

    for brewery_id in BREWERY_IDS:
        response = session.get(BREWERY + brewery_id)  # <7>
        resource_data = response.json()  # <8>
        brewery_data = resource_data['data']  # <9>
        brewery_name = brewery_data['name']
        brewery_website = brewery_data['website']
        print("{:30s} {}".format(brewery_name, brewery_website))
