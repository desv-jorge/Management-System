from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

def db_init():
    connect(db="Database" ,host=os.getenv("MONGO_URI"))

