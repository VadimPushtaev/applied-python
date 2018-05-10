from aiohttp import web
import asyncio

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = f'Hello {name}'
    return web.Response(text=text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle),
])

web.run_app(app)
