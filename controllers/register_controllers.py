from fastapi import HTTPException, status

from models.user import Model_user
from models.client import Model_client
from models.services import Model_services

from services.user_services import get_user_email_by_email, create_user
from services.client_services import create_client
from services.serviceDevice_services import create_service

from providers.hash_provider import gen_hash

async def processor_register_user(user : Model_user, logged_user):
    if (logged_user["acess_level"] != "admin"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Permissão necessária")

    isEmail = get_user_email_by_email(user.email)

    if(isEmail):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email em uso")
    
    password = str(user.password)
    password_hashed = gen_hash(password)

    return create_user(dict(user), password_hashed)

async def processor_register_client(client: Model_client, user_id):
    return create_client(dict(client), user_id)

async def processor_register_services(services: Model_services, user_id):
    return create_service(dict(services), user_id)