from pydantic import BaseModel

class Model_client(BaseModel):
    nome: str
    telefone: str | None = None
    email: str | None = None