
from aiohttp import web
from aiohttp_session import get_session
from src.data import select

routes = web.RouteTableDef()

@routes.post('/get/user_info')
async def get_user_info(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        if 'userId' in data:
            sel_obj = select.SelectData(params=data['userId'])
        else:
            sel_obj = select.SelectData(params=session_name)
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

@routes.post('/get/search_info')
async def get_search_info(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        sel_obj = select.SelectData(params=data)
        search_info = sel_obj.select_search_info()
        result = {
            "code": 200,
            "msg": "OK",
            "data": search_info
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/user_type')
async def get_user_type(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    if session_name:
        sel_obj = select.SelectData()
        user_type = sel_obj.select_user_type()
        result = {
            "code": 200,
            "msg": "OK",
            "data": user_type
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/departments')
async def get_departments(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    if session_name:
        sel_obj = select.SelectData()
        departments = sel_obj.select_departments()
        result = {
            "code": 200,
            "msg": "OK",
            "data": departments
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/professional')
async def get_professional(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        sel_obj = select.SelectData(data['departId'])
        professional = sel_obj.select_professional()
        result = {
            "code": 200,
            "msg": "OK",
            "data": professional
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/class')
async def get_professional(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        sel_obj = select.SelectData(data['professId'])
        classes = sel_obj.select_class()
        result = {
            "code": 200,
            "msg": "OK",
            "data": classes
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/semester')
async def get_semester(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    if session_name:
        sel_obj = select.SelectData()
        semester = sel_obj.select_semester()
        result = {
            "code": 200,
            "msg": "OK",
            "data": semester
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/course')
async def get_course(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    if session_name:
        sel_obj = select.SelectData()
        course = sel_obj.select_course()
        result = {
            "code": 200,
            "msg": "OK",
            "data": course
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/course_table')
async def get_course_table(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        sel_obj = select.SelectData(params=data)
        course_table = sel_obj.select_course_table()
        result = {
            "code": 200,
            "msg": "OK",
            "data": course_table
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/get/user_list')
async def get_teacher_list(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        sel_obj = select.SelectData(params=data)
        teacher_list = sel_obj.select_user_list()
        result = {
            "code": 200,
            "msg": "OK",
            "data": teacher_list
        }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)