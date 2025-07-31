from fastapi import APIRouter
from services.user_services import activate_account

router = APIRouter()

@router.patch("/status/{email}")
async def activate_user(email):
    return activate_account(str(email))