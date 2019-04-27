from aiohttp import web
from aiohttp_session import get_session
from src.data import update

routes = web.RouteTableDef()

@routes.post('/modify/user_info')
async def mod_user_info(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    data['userId'] = session_name
    if session_name:
        sel_obj = update.UpdateData(params=data)
        is_success = sel_obj.update_user_info()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 505,
                "msg": "Failed to modify data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)