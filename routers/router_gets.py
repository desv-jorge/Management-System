from fastapi import APIRouter

from services.user_get import get_user

from models.user import Model_user_one

router= APIRouter()

@router.get("/get/user")
async def user_get(email: Model_user_one):
    return await get_user(email.email)
