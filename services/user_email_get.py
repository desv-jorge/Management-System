from models.user import Model_user, Model_user_one
from database.connection import create_client

async def get_email(email: Model_user_one):
    client = create_client()

    db = client["Database"]
    collection = db["users"]

    results : Model_user = collection.find_one({"email": email})

    if(not results):
        return False
    
    results["_id"] = str(results["_id"])          

    client.close()
        
    return results["email"]

