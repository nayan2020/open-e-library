from time import monotonic
import mongoengine
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
