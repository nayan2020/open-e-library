import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from library.data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_file: str):  # put application's code'
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():  # put application's code here'
        raise Exception("You Must specify a db file")

    conn_str = 'sqlite:///' + db_file.strip()
    print(f'Connecting to DB with {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import library.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    session: Session = __factory()
    session.expire_on_commit = False
    return session
