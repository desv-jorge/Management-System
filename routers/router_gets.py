from fastapi import APIRouter, Depends
from models.user import Model_user
from routers import auth_utils
from controllers.get_controllers import services_get, clients_get

router = APIRouter()

@router.get("/services")
def get_services(user: Model_user = Depends(auth_utils.get_user_loggedIn)):
    return services_get()

@router.get("/clients")
def get_clients(user: Model_user = Depends(auth_utils.get_user_loggedIn)):
    return clients_get()