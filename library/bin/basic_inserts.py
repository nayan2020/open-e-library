import os

from library.data.releases import Release
from library.data import db_session
from library.data.package import Package


def main():
    init_db()
    while True:
        insert_a_package()


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()

    p.summary = input('Package summary: ').strip()
    p.description = input('Package description: ').strip()
    p.author_name = input('Author: ').strip()
    p.docs_url = input('Docs url: ').strip()
    p.license = input('License: ').strip()

    print("Release 1:")
    r = Release()
    r.major_ver = int(input("Major version: "))
    r.minor_ver = int(input("Minor version: "))
    r.build_ver = int(input("Build version: "))
    r.size = int(input("Size of Bytes: "))
    p.releases.append(r)

    # print("Release 2:")
    # r = Release()
    # r.major_ver = int(input("Major version: "))
    # r.minor_ver = int(input("Minor version: "))
    # r.build_ver = int(input("Build version: "))
    # r.size = int(input("Size of Bytes: "))
    # p.releases.append(r)

    session = db_session.create_session()
    session.add(p)
    session.commit()


def init_db():
    top_folder = os.path.dirname(__name__)
    rel_file = os.path.join('..', 'db', 'library.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
