from fastapi import APIRouter, HTTPException, status

from providers.hash_provider import verify_hash
from providers.token_provider import create_access_token

from models.auth import Model_login
from models.user import Model_user

from services.user_email_get import get_email
from services.user_get_hash_ByEmail import get_hash
from services.user_get_ByEmail import get_user

async def processor_login(data_login : Model_login):
    isEmail = await get_email(data_login.email)

    if(not isEmail):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email não possui cadastro")
    
    user = await get_user(data_login.email)

    if(user["is_active"] != True):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Email precisa ser autenticado")
    
    hash_password_bd : Model_user = await get_hash(data_login.email)

    password_isValid = verify_hash(data_login.password, hash_password_bd)

    if (not password_isValid):
        print("senha inválida")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "senha incorreta")
    
    token = create_access_token({"sub": data_login.email})
    
    return {"user": data_login, "acess_token": token}