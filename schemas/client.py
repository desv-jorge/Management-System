from mongoengine import Document, StringField
from datetime import datetime

class Client(Document):
    name = StringField(required=True)
    phone = StringField()
    email = StringField()
    created_at = StringField(default=lambda: datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    created_by = StringField(required=True)  # id do usuário que criou (String por simplicidade)

    meta = {
        'collection': 'clients'
    }
