from bson import ObjectId
from database.connection import create_client

def delete_client(id):
    client = create_client()

    db = client["Database"]
    collection = db["clients"]

    delete_response = collection.find_one_and_delete({"_id": ObjectId(id)})         

    client.close()
        
    return  delete_response