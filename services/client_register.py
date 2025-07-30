from database.connection import create_client
from datetime import datetime

client = create_client()

def create_client(name, phone, email, user_id):
    now = datetime.now()
    try:
        database = client["Database"]
        collection = database["clients"]

        document = { 
        "name" : name,
        "phone": phone,
        "email": email,
        "created_at": now.strftime("%d-%m-%Y %H:%M:%S"),
        "created_by": user_id
        }
    
        result = collection.insert_one(document)
        print(result)

        client.close()

        return {"is_register": True} if result.acknowledged else {"error": "failed"}

    except Exception as e:
        raise Exception(
            "erro: ", e)