from fastapi import APIRouter, Depends, Body

from models.user import Model_user
from models.client import Model_client
from models.services import Model_services

from controllers.register_controllers import processor_register_user, processor_register_client, processor_register_services
from .auth_utils import get_user_loggedIn

router = APIRouter()

@router.post("/user")
async def register_user(user_body: Model_user = Body(...), user: Model_user = Depends(get_user_loggedIn)):
    return await processor_register_user(user_body, user)

@router.post("/client")
async def register_client(user: Model_user = Depends(get_user_loggedIn), client: Model_client = Body(...)):
    return await processor_register_client(client, user.id)

@router.post("/services")
async def register_services(services: Model_services = Body(...),user: Model_user = Depends(get_user_loggedIn) ):
    return await processor_register_services(services, user.id)