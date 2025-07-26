from fastapi import APIRouter,Depends

from .auth_utils import get_user_loggedIn

from models.auth import Model_login
from models.user import Model_user

from controllers.auth_controllers import processor_login

router = APIRouter()

@router.post("/token")
async def login(data_login : Model_login):
    return await processor_login(data_login)

@router.get("/me")
def me(usuario: Model_user = Depends(get_user_loggedIn)):
    return usuario
    