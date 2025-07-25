from fastapi import APIRouter

from models.user import Model_user

from services.user_register import register_user

router = APIRouter()

@router.post("/register/user")
async def register_client(user: Model_user):
    return await register_user(user.name, user.level_acess, user.email, user.created_at)