#!/usr/bin/env python

import os
import asyncio
import aiofiles
import aiohttp

BASE_URL = 'http://stats.nba.com/stats'

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

DATA_FOLDER = '../TEMP/nba/asynch' # type: str


def main():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER, exist_ok=True)

    loop = asyncio.get_event_loop()
    player_args = []
    loop.run_until_complete(get_players(player_args))
    print("Fetched {} players.".format(len(player_args)))
    loop.run_until_complete(
        asyncio.gather(
            *(get_player(*args) for args in player_args)
        )
    )

async def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = BASE_URL + endpoint
    print('Getting all players...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as resp:
            data = await resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])

async def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = BASE_URL + endpoint
    print('Getting player', player_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as resp:
            print(resp)
            data = await resp.text()

    file_name = player_name.replace(" ", "_") + '.json'
    file_path = os.path.join(DATA_FOLDER, file_name)

    async with aiofiles.open(file_path, 'w') as file:
        await file.write(data)


if __name__ == '__main__':
    main()
