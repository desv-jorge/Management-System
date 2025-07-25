from database.connection import create_client

client = create_client()

async def register_user(name, level_acess, email ,password , created_at):
    try:
        database = client["Database"]
        collection = database["users"]

        document = { 
        "nome" : name,
        "acess_level" : level_acess,
        "email": email,
        "password": password,
        "created_at": created_at }
    

        result = collection.insert_one(document)

        print(result.acknowledged)
        client.close()

        return {"success": "ok"} if result.acknowledged else {"error": "failed"}

    except Exception as e:
        raise Exception(
            "erro: ", e)