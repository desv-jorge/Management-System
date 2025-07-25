from fastapi import APIRouter, HTTPException, status
from providers.hash_provider import verify_hash
import json

from models.auth import Model_login
from models.user import Model_user

from services.user_email_get import get_email
from services.user_hash_get import get_hash

router = APIRouter()

@router.post("/token")
async def login(data_login : Model_login):
    isEmail = await get_email(data_login.email)

    if(not isEmail):
        print("não existe")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email não possui cadastro")
    
    hash_password_bd : Model_user = await get_hash(data_login.email)
    hash_bd = hash_password_bd["password"]
    print(hash)

    password_isValid = verify_hash(data_login.password, hash_bd)

    if (not password_isValid):
        print("senha inválida")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "senha incorreta")
    
    return {"sucess": "ok"}
    