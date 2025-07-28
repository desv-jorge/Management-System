from database.connection import create_client

def delete_user(email):
    client = create_client()

    db = client["Database"]
    collection = db["users"]

    user = collection.find_one_and_delete({"email": email})      

    client.close()
        
    return  user

