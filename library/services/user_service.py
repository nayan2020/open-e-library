from typing import Optional

from passlib.hash import pbkdf2_sha256 as crypto
from library.nosql.users import User


def get_user_count() -> int:
    return User.objects().count()


def find_user_by_email(email: str) -> Optional[User]:
    user = User.objects(email=email).first()
    return user


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        print(f"ERROR: Account with email {email} already exists.")
        return None

    user = User()
    user.email = email
    user.name = name
    user.hashed_password = hash_text(password)

    user.save()

    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.using(round(171204)).hash(text)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    user = find_user_by_email(email)

    # print("mongodb return: "+str({"hashed_password":obje user}))
    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None
    print("login_end user ser")
    return user


def find_user_by_id(user_id: int) -> Optional[User]:
    user = User.objects().filter(id=user_id).first()
    return user
