
from src import config
from src.http import login
from aiohttp import web

app = web.Application()
app.add_routes(login.routes)
web.run_app(app, host=config.host, port=config.port)