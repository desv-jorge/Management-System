from pydantic import BaseModel

class Model_user(BaseModel):
    name: str
    level_acess: str
    email: str
    password: str
    created_at: str | None

class Model_user_one(BaseModel):
    email: str
