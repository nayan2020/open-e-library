from typing import Optional

import flask
from flask import Request

from library.infrastructure import cookie_auth, request_dict


class ViewModelBase:
    def __int__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create()

        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie_auth.get_user_id_via_auth_cookie(self.request)

    def to_dict(self):
        return self.__dict__
