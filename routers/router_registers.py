from fastapi import APIRouter

from models.user import Model_user

from services.user_register import register_user
from providers.hash_provider import gen_hash

router = APIRouter()

@router.post("/register/user")
async def register_client(user: Model_user):
    password = gen_hash(user.password)
    return await register_user(user.name, user.level_acess, user.email, password ,user.created_at)