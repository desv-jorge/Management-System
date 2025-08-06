from schemas.services import Service

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