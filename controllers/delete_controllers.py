from models.user import Model_user, email

from services.user_services import delete_user
from services.client_services import delete_client
from services.serviceDevice_services import delete_services

from fastapi import HTTPException, status


async def user_delete(email: email, user: Model_user):
    if (user["acess_level"] != "admin"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Permissão necessária")

    delete_response = dict(delete_user(str(email["email"])))

    if(delete_response['response'] == False):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Usuário deletado com sucesso")

async def client_delete(id):
    delete_response = dict(delete_client(id))

    if(delete_response['response'] == True):
        raise HTTPException(status_code=status.HTTP_200_OK, detail="client deletado com sucesso")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="client não encontrado")

async def services_delete(id):
    delete_response = dict(delete_services(id))

    if(delete_response['response'] == True):
        raise HTTPException(status_code=status.HTTP_200_OK, detail="service deletado com sucesso")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="service não encontrado")