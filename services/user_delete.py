from models.user import Model_user
from database.connection import create_client

from .user_get_ByEmail import get_user

async def delete_user(email):
    client = create_client()

    db = client["Database"]
    collection = db["users"]

    user : Model_user = await get_user(email.email)
    
    if(not user):
        return False

    collection.delete_one({"email": user["email"]})         

    client.close()
        
    return  True

