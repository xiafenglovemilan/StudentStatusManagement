# -*- coding: utf-8 -*-

from src.data import select
from aiohttp import web

routes = web.RouteTableDef()

@routes.post('/login')
async def login(request):
    data = await request.json()
    sel_obj = select.SelectData(data['name'])
    pass_wd = sel_obj.select_password()
    result = {}
    if pass_wd == data['pass_wd']:
        result['code'] = 200
        result['msg'] = "OK"
        result['data'] = {}
    else:
        result['code'] = 500
        result['msg'] = "error"
        result['data'] = {}

    return web.json_response(result)