from fastapi import APIRouter, Depends, Body

from models.user import Model_user

from controllers.register_controllers import processor_register_user

from .auth_utils import get_user_loggedIn

router = APIRouter()

@router.post("/user")
async def register_user(user: Model_user = Depends(get_user_loggedIn), user_body: Model_user = Body()):
    return await processor_register_user(user_body)