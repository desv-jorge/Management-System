from models.user import Model_user
from database.connection import create_client

def get_hash(email):
    client = create_client()

    db = client["Database"]
    collection = db["users"]

    results : Model_user = collection.find_one({"email": email})
    
    if(not results):
        return False
    
    results["_id"] = str(results["_id"])          

    client.close()
        
    return results["password"]

