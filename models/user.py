from pydantic import BaseModel

class Model_simple_user(BaseModel):
    name: str
    level_acess: str
    email: str

class Model_user(BaseModel):
    name: str
    level_acess: str
    email: str
    password: str
    created_at: str | None

class Model_user_one(BaseModel):
    email: str
