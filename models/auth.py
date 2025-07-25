from pydantic import BaseModel

class Model_login(BaseModel):
    email: str
    password: str