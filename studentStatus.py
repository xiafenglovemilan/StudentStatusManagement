
from src import config
from src.http import login
from src.http import getInfo
from src.http import addInfo
from aiohttp import web
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import base64

app = web.Application()
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key, max_age=3600, cookie_name='USER_SESSION'))
app.add_routes(login.routes)
app.add_routes(getInfo.routes)
app.add_routes(addInfo.routes)
web.run_app(app, host=config.host, port=config.port)