from fastapi import APIRouter
from controllers.modify_controllers import mofify_status

router = APIRouter()

@router.patch("/status/{email}")
async def activate_user(email):
    print(f"rota| edit_status: {email}")
    return await mofify_status(str(email))