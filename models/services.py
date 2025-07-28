from pydantic import BaseModel
from typing import Optional

class Model_services(BaseModel):
    client : str
    device: str
    description: str
    email: Optional[str] = None