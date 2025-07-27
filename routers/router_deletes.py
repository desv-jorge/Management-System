from fastapi import APIRouter, Depends, Body, Path ,HTTPException, status

from models.user import Model_user_one, Model_user

from .auth_utils import get_user_loggedIn
from controllers.delete_controllers import user_delete
from controllers.delete_controllers import client_delete


router = APIRouter()

@router.delete("/user")
async def delete_user(user: Model_user = Depends(get_user_loggedIn), email_body: Model_user_one =Body()):
    return await user_delete(email_body, user)

@router.delete("/client/{id}")
async def delete_client(id: str = Path(), user: Model_user = Depends(get_user_loggedIn)):
    return await client_delete(id)