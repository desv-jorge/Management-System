from schemas.client import Client
from schemas.user import User
from mongoengine.errors import ValidationError, NotUniqueError, DoesNotExist


def create_client(client_body, user_id: str):
    try:
        client = Client(
            name=client_body["name"],
            phone=client_body["phone"],
            email=client_body["email"],
            created_by= str(user_id)
        )
        client.save()
        return {"is_register": True, "client_id": str(client.id)}
    
    except (ValidationError, NotUniqueError) as e:
        return {"error": str(e)}
    
    except Exception as e:
        raise Exception(f"Erro ao criar cliente: {e}")

def delete_client(id: str):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return {"response": True}

    except (DoesNotExist, ValidationError):
        return {"response": False}

    except Exception as e:
        raise Exception(f"Erro ao deletar cliente: {e}")