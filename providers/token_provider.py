from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv
import os
from jose import jwt # pyright: ignore[reportMissingModuleSource]

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    new_data = data.copy()
    expirate = datetime.now(timezone.utc) + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)

    new_data.update({"exp": expirate})

    token_jwt = jwt.encode(new_data, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verify_acess_token(token: str):

    load = jwt.decode(token , SECRET_KEY, algorithms=[ALGORITHM])

    return load.get("sub")