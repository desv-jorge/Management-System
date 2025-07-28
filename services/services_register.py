from database.connection import create_client
from datetime import datetime

client = create_client()

async def create_services(client_req, device , desc, email, user):
    now = datetime.now()
    try:
        database = client["Database"]
        collection = database["services"]

        document = { 
        "client" : client_req,
        "device": device,
        "description": desc,
        "email": email,
        "created_at": now.strftime("%d-%m-%Y %H:%M:%S"),
        "created_by": user 
        }
    
        result = collection.insert_one(document)
        print(result)

        client.close()

        return {"is_register": True} if result.acknowledged else {"error": "failed"}

    except Exception as e:
        raise Exception("erro: ", e)