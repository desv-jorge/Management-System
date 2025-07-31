from database.connection import db_init
from schemas.user import User
from mongoengine.errors import ValidationError

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

def delete_user(email_res:str):
    try:
        user_to_delete = User.objects(email=email_res).first()

        if user_to_delete == None:
            return {"response": False}
        
        user_to_delete.delete()
        return {"response": True}

    except ValidationError:
        return {"response": False}

    except Exception as e:
        raise Exception(f"Erro ao deletar usuário: {e}")

def get_user_email_by_email(email: str) -> str | None:
    user = User.objects(email=email).only("email").first()
    if user:
        return user.email
    return None

def get_user_by_email(email: str) -> User | None:
    user = User.objects(email=email).first()
    return user

def activate_account(email: str):

    try:
        user = User.objects(email=email).first()

        if not user:
            return {"error": "Usuário não encontrado"}

        user.is_active = True
        user.save()

        return {"message": "Usuário ativado com sucesso"}

    except Exception as e:
        raise Exception(f"Erro ao ativar usuário: {e}")
