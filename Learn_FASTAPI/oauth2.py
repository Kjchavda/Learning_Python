from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import schemas

SECRET_KEY = "e3b8579016219202862a342efbb9b2d27a3cecd863cf25291ca2ef6e15220dd4"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRY_TIME = 30

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=ACCESS_TOKEN_EXPIRY_TIME)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.Token_data(id=id)
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token:str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-authenticate":"Bearer"})
    return verify_access_token(token, credentials_exception)

