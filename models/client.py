from pydantic import BaseModel
from typing import Optional

class Model_client(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None