from fastapi import HTTPException, status

from models.user import Model_user

from services.user_register import register_user
from services.user_email_get import get_email

from providers.hash_provider import gen_hash

async def processor_register_user(user : Model_user):
    print(f"\n argumento: {user}")

    isEmail = await get_email(user.email)
    print(f"\n {isEmail}")

    if(isEmail):
        print("existe")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email em uso")
    
    password = str(user.password)
    password_hashed = gen_hash(password)
    return await register_user(user.name, user.level_acess, user.email, password_hashed)