import asyncio
import json

import aiohttp


async def get_score_and_print(i):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8081/{}'.format(i)) as resp:
            print(await resp.text())


async def main():
    i = 0
    while True:
        i += 1
        asyncio.ensure_future(get_score_and_print(i))
        await asyncio.sleep(0.01)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())