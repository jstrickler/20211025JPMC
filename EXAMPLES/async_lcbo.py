#!/usr/bin/env python
#
import asyncio
import aiohttp

AUTH_TOKEN = 'CJAssociatesTraining'  # <1>
AUTH_KEY = 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'

BASE_URL_TEMPLATE = 'http://lcboapi.com/products?q={}'  # <2>

SEARCH_TERMS = [  # <3>
    'stolichnaya', 'makers mark', 'woodford', 'wombat', 'molson', 'moosehead',
    'michelob', 'bacardi', 'old rotgut', 'four roses', 'moonshine', 'harvest',
    'captain morgan', 'tanqueray', 'green spot', 'chartreuse'
]

def main():
    loop = asyncio.get_event_loop()  # <4>
    auth = aiohttp.BasicAuth(AUTH_TOKEN, AUTH_KEY)  # <5>

    with aiohttp.ClientSession(loop=loop, auth=auth) as client_session: # <6>

        task_list = [
            loop.create_task(fetch_matches(client_session, search_term)) for search_term in SEARCH_TERMS
        ]  # <7>

        loop.run_until_complete(asyncio.wait(task_list)) # <7>


async def fetch_data(client_session, search_term):  #
    url = BASE_URL_TEMPLATE.format(search_term.replace(' ', '+'))
    async with client_session.get(url) as resp:  # <8>
        assert resp.status == 200
        return await resp.json()  # <9>

async def fetch_matches(client_session, search_term):
        data = await fetch_data(client_session, search_term)
        names = []

        if data['result']:
            for result in data['result']:
                names.append(result['name'])
        print('{}: '.format(search_term.upper()), ';'.join(names))


if __name__ == "__main__":
    main()
