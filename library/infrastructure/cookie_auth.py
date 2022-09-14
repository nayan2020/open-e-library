import hashlib
import datetime
from typing import Optional

from flask import Response, Request
import library.services.user_service as user_service

auth_cookie_name = 'library_cookie'


def set_auth(response: Response, user_id: int):
    hash_val = user_service.__hash_text(user_id)
    val = "{}:{}".format(user_id, hash_val)
    response.set_cookie(auth_cookie_name, val)


def __hash_text(text: str) -> str:
    text = 'salty__' + text + '__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def __add_cookie_callback(_, response: Response, name: str, value: str):
    response.set_cookie(name, value, max_age=datetime.timedelta(days=1))


def get_user_id_via_auth_cookie(request: Request) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = int(parts[0])
    hash_val = parts[1]
    hash_val_check = user_service.__hash_text(user_id)
    if hash_val != hash_val_check:
        print("Warning : Hash mismatch, invalid cookie value")
        return None

    return user_id


def logout(response: Response):
    response.delete_cookie(auth_cookie_name)
