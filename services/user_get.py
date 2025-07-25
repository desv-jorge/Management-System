from models.user import Model_user
from mongo.connection import create_client

async def get_user(email):
    client = create_client()

    try:
        db = client["Database"]
        collection = db["users"]

        results : Model_user = collection.find_one({"email": email})
        results["_id"] = str(results["_id"])
            
        print(results)

        client.close()

        return results
    except Exception as e:
        raise Exception("erro: ", e)
