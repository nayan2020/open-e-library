
from typing import Optional

import sqlalchemy.orm as orm
from library.data.package import Package
from library.data.releases import Release
from library.data import db_session


# def get_latest_packages():
#     return [
#         {'name': 'click ', 'version': '8.1.3'},
#         {'name': 'Flask ', 'version': '2.1.2'},
#         {'name': 'greenlet ', 'version': '1.1.2'},
#         {'name': 'importlib - metadata ', 'version': '4.11.3'},
#         {'name': 'itsdangerous ', 'version': '2.1.2'},
#         {'name': 'Jinja2 ', 'version': '3.1.2'},
#         {'name': 'MarkupSafe ', 'version': '2.1.1'},
#         {'name': 'SQLAlchemy ', 'version': '1.4.36'},
#         {'name': 'Werkzeug ', 'version': '2.1.2'},
#         {'name': 'zipp ', 'version': '3.8.0'},
#     ]
def get_latest_releases(limit=4):  # -> List[Release]
    session = db_session.create_session()

    releases = session.query(Release). \
        options(orm.joinedload(Release.package)). \
        order_by(Release.created_date.desc()). \
        limit(limit). \
        all()
    # limit(limit).\
    session.close()
    return releases


def get_release_count() -> int:
    session = db_session.create_session()
    return session.query(Release).count()


def get_package_count() -> int:
    session = db_session.create_session()
    return session.query(Package).count()


def get_package_by_id(package_id: str) -> Optional[Package]:
    if not package_id:
        return None

    package_id = package_id.strip().lower()
    session = db_session.create_session()

    package = session.query(Package). \
        options(orm.joinedload(Package.releases)).\
        filter(Package.id == package_id).\
        first()

    session.close()
    return package
