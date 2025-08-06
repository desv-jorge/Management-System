from schemas.services import Service
from schemas.client import Client

def services_get():
    
    services = Service.objects()
    services_list = []

    for service in services:
        services_list.append({
            "id": str(service.id),
            "client": service.client,
            "device": service.device,
            "description": service.description,
            "email": service.email,
            "created_by": str(service.created_by),
            "created_at": service.created_at  # já é string!
        })

    return services_list

def clients_get():

    clients = Client.objects()
    clients_list = []

    for client in clients:
        clients_list.append({
            "id": str(client.id),
            "name": client.name,
            "phone": client.phone,
            "email": client.email,
            "created_by": str(client.created_by),
            "created_at": client.created_at  # já é string
        })

    return clients_list