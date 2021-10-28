import sys
import requests
from pprint import pprint

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>


def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    response = requests.get(
        BASE_URL + args[0],   # URL + search term
        params={'key': API_KEY},  # GET parameters   foo=bar&spam=ham ....
        # auth=(auth_name, auth_value),   #username/pw
        # data={...},  # dict of data for POST
        # cookies={....|,  # one or more cookies}
        # headers={h1:v1, h2: v2},
        # proxies={'https': 'myproxy.mycompany.com:12345'},
        # verify=False,
        # json={'foo': 'bar'},
        # cert='path/to/cert/file',
    )  # <3>

    if response.status_code == requests.codes.OK:  # 200?
        data = response.json()  # <4>  # convert JSON to python data structure
        # data = json.loads(response.content)
        # data.content   raw (binary) content   Unicode is encoded in .content
        # data.text  python Unicode string  same as data.content.decode()
        # data.json()  result of calling json.loads(response.content)
        pprint(data)
        for entry in data: # <5>
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = '({})'.format(entry.get('fl'))
                    word_id = meta.get("id")
                    print("{} {}".format(word_id.upper(), part_of_speech))
                if "shortdef" in entry:
                    print('\n'.join(entry['shortdef']))
                print()
            else:
                print(entry)

    else:
        print("Sorry, HTTP response", response.status_code)

    # with requests.Session() as session:
    #     session.auth = ("foo", 'bar')
    #     session.verify=false
    #
    #     result = session.get('http://www.python.org')

if __name__ == '__main__':
    main(sys.argv[1:])
