#!/usr/bin/env python
"""
Async reddit example based on
https://stackabuse.com/python-async-await-tutorial/
"""
import sys
import signal

import asyncio
import aiohttp
import json

REDDIT_SITES = ['python', 'programming', 'MapsWithoutNZ'] # <1>


def main():
    loop = asyncio.get_event_loop()  # <2>

    client = aiohttp.ClientSession(loop=loop) # <3>

    signal.signal(signal.SIGINT, signal_handler)  # <4>

    for reddit_site in REDDIT_SITES[:]:
        asyncio.ensure_future(get_reddit_top(reddit_site, client)) # <5>

    loop.run_forever() # <6>


async def get_json(client, url):
    async with client.get(url) as response: # <7>
        assert response.status == 200 # <8>
        return await response.read()  # <9>

async def get_reddit_top(subreddit, client):
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5') # <10>


    j = json.loads(data1.decode('utf-8')) # <11>
    # pprint(j)
    # print('-' * 60)
    for i in j['data']['children']:  # <12>
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')
    print('-' * 60 + '\n')

def signal_handler(signal, frame): # <13>
    loop.stop()
    client.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
