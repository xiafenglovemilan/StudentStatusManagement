
from aiohttp import web
from aiohttp_session import get_session
from src.data import select

routes = web.RouteTableDef()

@routes.post('/get/user_info')
async def get_user_info(request):
    session = await get_session(request)
    session_name = session['name'] if 'name' in session else None
    if session_name:
        sel_obj = select.SelectData(session_name)
        user_info = sel_obj.select_user_info()
        result = {
            "code": 200,
            "msg": "OK",
            "data": user_info
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)
