from schemas.services import Service
from schemas.user import User
from mongoengine.errors import ValidationError, DoesNotExist
from bson import ObjectId

def create_service(service_body, user_id: str):
    try:
        user = User.objects(id=ObjectId(user_id)).first()

        if not user:
            return {"error": "Usuário não encontrado"}

        service = Service(
            client=service_body["client"],
            device=service_body["device"],
            description=service_body["description"],
            email=service_body["email"],
            created_by=str(user_id)
        )
        service.save()

        return {"is_register": True, "service_id": str(service.id)}

    except ValidationError as e:
        return {"error": str(e)}
    
    except Exception as e:
        raise Exception(f"Erro ao criar serviço: {e}")

def delete_services(id: str):
    try:
        service = Service.objects.get(id=id)
        service.delete()
        return {"response": True}

    except (DoesNotExist, ValidationError):
        return {"response": False}

    except Exception as e:
        raise Exception(f"Erro ao deletar serviço: {e}")
    
def services_get():
    pass