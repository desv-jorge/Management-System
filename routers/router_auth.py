from fastapi import APIRouter, HTTPException, status
from providers.hash_provider import verify_hash, gen_hash
from providers.token_provider import create_access_token, verify_acess_token
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
    
    print(hash_password_bd)

    password_isValid = verify_hash(data_login.password, hash_password_bd)

    if (not password_isValid):
        print("senha inválida")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "senha incorreta")
    
    token = create_access_token({"sub": data_login.email})
    
    return {"user": data_login, "acess_token": token}

@router.get("/me")
def me(token: str):
    return 
    