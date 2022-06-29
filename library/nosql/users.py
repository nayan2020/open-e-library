from time import monotonic
import library.infrastructure.cookie_auth as cookie_auth
import mongoengine
import flask
from typing import Optional
import bson
from flask import Response
import datetime


class User(mongoengine.Document):
    name = mongoengine.StringField()
    email = mongoengine.StringField()
    hashed_password = mongoengine.StringField(unique=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'collection': 'users',
        'db_alias': 'core',
        'indexes': [
            'email',
            'hashed_password',
            'created_date'
        ]

    }

    # def get_user(self):
    #     return {
    #         "name": self.name,
    #         "email": self.email,
    #         "hashed_password": self.hashed_password,
    #         "created_date": self.created_date,
    #         "error": Optional[str] = None
    #         "user_id": cookie_auth.get_user_id_via_auth_cookie(flask.request),
    #
    #     }
