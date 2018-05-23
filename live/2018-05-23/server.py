from aiohttp import web

routes = web.RouteTableDef()


def process_batch(batch):
    return [x ** 3 for x in batch]


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@routes.post('/')
async def get_score(request):
    data = await request.json()
    print(data)

    return web.json_response(process_batch(data))


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
