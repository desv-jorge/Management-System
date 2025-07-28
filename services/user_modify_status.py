from database.connection import create_client
from datetime import datetime

client = create_client()

def edit_status(email: str):
    print(f"edit_status: {email}")

    try:
        database = client["Database"]
        collection = database["users"]

        query_filter = {'email' : email}
        update_operation = { '$set' : { 'is_active' : True }}

        results = collection.update_one(query_filter, update_operation)


        client.close()

        return {"message": "usuário ativo"}


    except Exception as e:
        raise Exception(
            "erro: ", e)