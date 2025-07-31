from mongoengine import Document, StringField
from datetime import datetime

class Service(Document):
    client = StringField(required=True)       # nome ou id do cliente (dependendo do uso)
    device = StringField(required=True)
    description = StringField(required=True)
    email = StringField()
    created_at = StringField(default=lambda: datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    created_by = StringField(required=True)

    meta = {
        'collection': 'services'
    }
