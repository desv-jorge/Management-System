from fastapi import APIRouter, HTTPException, status

from providers.hash_provider import verify_hash
from providers.token_provider import create_access_token

from models.auth import Model_login

from services.user_services import get_user_email_by_email, get_user_by_email

async def processor_login(data_login : Model_login):
    isEmail = get_user_email_by_email(data_login.email)

    if(not isEmail):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email não possui cadastro")
    
    user = get_user_by_email(data_login.email)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email não possui cadastro")

    if(user["is_active"] != True):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Email precisa ser autenticado")
    
    hash_password_bd = user["password"]

    password_isValid = verify_hash(data_login.password, hash_password_bd)


    if (not password_isValid):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "senha incorreta")
    
    token = create_access_token({"sub": data_login.email})
    
    return {"user": data_login, "acess_token": token}