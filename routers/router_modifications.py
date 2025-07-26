from fastapi import APIRouter
from controllers.modify_controllers import mofify_status

router = APIRouter()

@router.patch("/status/{email}")
async def edit_status(email):
    print(f"rota| edit_status: {email}")
    return await mofify_status(str(email))