#!/usr/bin/env python

import asyncio
from aiohttp import ClientSession

from sampleurls import URLS


async def fetch(url, session):
    async with session.get(url) as response:  # <1>
        return await response.read()  # return content from response


async def run():
    tasks = []

    async with ClientSession() as session: # <2>
        for url in URLS:
            task = asyncio.ensure_future(fetch(url, session))  # <3>
            tasks.append(task)

        responses = await asyncio.gather(*tasks)  # <4>
        return responses  # <5>


def print_responses(result):
    print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # <6>
    future = asyncio.ensure_future(run())
    loop.run_until_complete(future)
    for result in future.result():
        print(result[:1000].decode() + '\n')
        print('*' * 60)


