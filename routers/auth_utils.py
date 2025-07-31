from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError

from providers.token_provider import verify_acess_token
from services.user_services import get_user_email_by_email

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

async def get_user_loggedIn(token: str = Depends(oauth2_schema)):
    error_excepetion = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        email = verify_acess_token(token)

    except JWTError:
        raise error_excepetion
    
    if not email:
        raise error_excepetion
    
    user = await get_user_email_by_email(email)

    if user == None:
        raise error_excepetion

    return user