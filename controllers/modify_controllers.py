from services.user_modify_status import edit_status

async def mofify_status(email: str):
    print(f"modify_status: {email}")
    response = await edit_status(email)

    return response