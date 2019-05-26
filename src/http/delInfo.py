from aiohttp import web
from aiohttp_session import get_session
from src.data import delete

routes = web.RouteTableDef()

@routes.post('/delete/class')
async def del_class(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        del_obj = delete.DeleteData(params=data)
        is_success = del_obj.delete_class()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 506,
                "msg": "Failed to delete data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/delete/professional')
async def del_professional(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        del_obj = delete.DeleteData(params=data)
        is_success = del_obj.delete_professional()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 506,
                "msg": "Failed to delete data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/delete/departments')
async def del_departments(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        del_obj = delete.DeleteData(params=data)
        is_success = del_obj.delete_departments()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 506,
                "msg": "Failed to delete data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/delete/user_info')
async def del_user_info(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        del_obj = delete.DeleteData(params=data)
        is_success = del_obj.delete_user_info()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 506,
                "msg": "Failed to delete data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)