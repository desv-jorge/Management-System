# models/user.py
from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime

class User(Document):
    name = StringField(required=True)
    acess_level = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    created_at = StringField(default=lambda: datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    status = StringField(default="active")
    is_active = BooleanField(default=False)

    meta = {
        'collection': 'users'
    }
