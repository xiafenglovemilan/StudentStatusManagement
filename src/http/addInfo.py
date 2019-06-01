from aiohttp import web
from aiohttp_session import get_session
from src.data import insert

routes = web.RouteTableDef()

@routes.post('/add/member_info')
async def add_member_info(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        data = insert_obj.add_member_info()
        if 'userId' in data:
            result = {
                "code": 200,
                "msg": "OK",
                "data": data
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/departments')
async def add_departments(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_departments()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/professional')
async def add_professional(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_professional()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/class')
async def add_class(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_class()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/course_table')
async def add_course_table(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_course_table()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/course')
async def add_course(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_course()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/semester')
async def add_semester(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_semester()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)

@routes.post('/add/student_grade')
async def add_student_grade(request):
    session = await get_session(request)
    session_name = session['userId'] if 'userId' in session else None
    data = await request.json()
    if session_name:
        insert_obj = insert.InsertData(data)
        is_success = insert_obj.add_student_grade()
        if is_success:
            result = {
                "code": 200,
                "msg": "OK",
                "data": {}
            }
        else:
            result = {
                "code": 504,
                "msg": "Failed to add data",
                "data": {}
            }
    else:
        result = {
            "code": 503,
            "msg": "Not logged in",
            "data": {}
        }
    return web.json_response(result)