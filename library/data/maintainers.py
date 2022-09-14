import sqlalchemy
from library.data.modelbase import SqlAlchemyBase


class Maintainer(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    package = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
