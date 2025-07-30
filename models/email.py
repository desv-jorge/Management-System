from pydantic import BaseModel

class Model_email_confirm(BaseModel):
    name: str
    email: str
    code: str