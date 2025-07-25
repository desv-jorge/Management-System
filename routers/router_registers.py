from fastapi import APIRouter, HTTPException, status

from models.user import Model_user

from services.user_register import register_user
from services.user_get import get_user

from providers.hash_provider import gen_hash

router = APIRouter()

@router.post("/register/user")
async def register_client(user: Model_user):
    isEmail = await get_user(user.email)
    if(isEmail):
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email em uso")
        
    password = gen_hash(user.password)
    return await register_user(user.name, user.level_acess, user.email, password ,user.created_at)