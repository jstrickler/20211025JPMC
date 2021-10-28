import requests

response = requests.get('http://www.python.org')
if response.status_code == requests.codes.OK:
    print(response.text)
else:
    print("Unable to retrieve page")