import asyncio
import json

import aiohttp

from aiohttp import web

routes = web.RouteTableDef()


class Queue:
    _INSTANCE = None

    def __init__(self):
        self._queue = []

    @classmethod
    def get_instance(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE = cls()

        return cls._INSTANCE

    def add(self, product_id, future):
        self._queue.append((product_id, future))

    async def infinite_process(self):
        while True:
            await asyncio.sleep(1)
            current_queue = self._queue[:]

            if current_queue:  # [(1, f1), (2, f2), (3, f3)]
                async with aiohttp.ClientSession() as session:
                    product_ids = [product_id for product_id, future in current_queue]
                    print(product_ids)
                    async with session.post('http://localhost:8080/', data=json.dumps(product_ids)) as resp:
                        response_data = await resp.json()  # [1, 8, 27]
                        for i, score in enumerate(response_data):
                            product_id, future = current_queue[i]
                            future.set_result(score)

                self._queue = []


def process_batch(batch):
    return [x ** 3 for x in batch]


async def get_score(product_id):
    future = asyncio.get_event_loop().create_future()
    Queue.get_instance().add(product_id, future)

    return await future


@routes.get('/{product_id}')
async def get_data(request):
    product_id = int(request.match_info['product_id'])

    return web.json_response(await get_score(product_id))


def main():
    asyncio.get_event_loop().create_task(Queue.get_instance().infinite_process())
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=8081)


if __name__ == '__main__':
    main()
