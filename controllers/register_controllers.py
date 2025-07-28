from fastapi import HTTPException, status

from models.user import Model_user
from models.client import Model_client
from models.services import Model_services

from services.user_register import register_user
from services.client_register import create_client
from services.services_register import create_services
from services.user_email_get import get_email

from providers.hash_provider import gen_hash

async def processor_register_user(user : Model_user, logged_user ):
    if (logged_user["acess_level"] != "admin"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Permissão necessária")

    isEmail = await get_email(user.email)

    if(isEmail):
        print("existe")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email em uso")
    
    password = str(user.password)
    password_hashed = gen_hash(password)

    return await register_user(user.nome, user.acess_level, user.email, password_hashed)

async def processor_register_client(client: Model_client, user_id):
    return await create_client(client.nome, client.telefone, client.email, user_id)

async def processor_register_services(services: Model_services, user_id):
    return await create_services(services.client,services.device ,services.description, services.email, user_id)