from pydantic import BaseModel

class Model_email_confirm(BaseModel):
    nome: str
    email: str
    codigo: str