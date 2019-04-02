
import asyncio

from aiohttp import web

async def index(request):
    return web.Response(status=200, body='{"code": 200, "msg": "OK", "data": {}}')

async def init(loop):
    app = web.Application()
    app.router.add_route('POST', '/', index)
    srv = await loop.create_server(app.make_handler(), "127.0.0.1", 8888)
    print("Server started at http://127.0.0.1:8888...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()