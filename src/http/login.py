# -*- coding: utf-8 -*-

from src.data import select
from aiohttp import web
from aiohttp_session import get_session
routes = web.RouteTableDef()

@routes.post('/login')
async def login(request):
    data = await request.json()
    session = await get_session(request)
    result = {}
    session_name = session['studentId'] if 'studentId' in session else None
    session_password = session['pass_wd'] if 'pass_wd' in session else None
    if data['pass_wd'] == session_password and data['studentId'] == session_name:
        result['code'] = 501
        result['msg'] = "User logged in"
        result['data'] = {}
    else:
        sel_obj = select.SelectData(data['studentId'])
        pass_wd = sel_obj.select_password()
        if pass_wd == data['pass_wd']:
            result['code'] = 200
            result['msg'] = "OK"
            result['data'] = {}
            session['studentId'] = data['studentId']
            session['pass_wd'] = data['pass_wd']
        else:
            result['code'] = 502
            result['msg'] = "Incorrect studentId or password"
            result['data'] = {}
    return web.json_response(result)

@routes.post('/logout')
async def logout(request):
    session = await get_session(request)
    session.invalidate()
    result = {
        'code': 200,
        'msg': "OK",
        'data': {}
    }
    return web.json_response(result)