from fastapi import APIRouter, Depends, Body

from models.user import Model_user_one

from .auth_utils import get_user_loggedIn
from controllers.delete_controllers import user_delete

router = APIRouter()

@router.delete("/user")
async def delete_user(email: Model_user_one = Depends(get_user_loggedIn), email_body: Model_user_one =Body()):
    await user_delete(email_body)