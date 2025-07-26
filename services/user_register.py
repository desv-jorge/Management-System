from database.connection import create_client
from datetime import datetime

client = create_client()

async def register_user(nome, acess_level, email ,password):
    now = datetime.now()
    try:
        database = client["Database"]
        collection = database["users"]

        document = { 
        "nome" : nome,
        "acess_level" : acess_level,
        "email": email,
        "password": password,
        "created_at": now.strftime("%d-%m-%Y %H:%M:%S"),
        "is_active": False 
        }
    
        result = collection.insert_one(document)
        print(result)

        client.close()

        return {"message": "usuário registrado"} if result.acknowledged else {"error": "failed"}

    except Exception as e:
        raise Exception(
            "erro: ", e)