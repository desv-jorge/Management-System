from fastapi import APIRouter
from controllers.modify_controllers import mofify_status

router = APIRouter()

@router.patch("/status/{email}")
async def activate_user(email):
    return await mofify_status(str(email))