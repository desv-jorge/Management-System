from database.connection import db_init
from schemas.user import User

db_init()

def create_user(data_user: dict, password: str):
    user = User(
        name= data_user["name"],
        acess_level= data_user["acess_level"],
        email= data_user["email"],
        password= password,
    )
    user.save()

    return user

def get_user_email_by_email(email: str) -> str | None:
    user = User.objects(email=email).only("email").first()
    if user:
        return user.email
    return None

def get_user_by_email(email: str) -> User | None:
    user = User.objects(email=email).first()
    return user