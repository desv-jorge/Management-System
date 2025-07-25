# db/connection.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env

def create_client():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    return client
