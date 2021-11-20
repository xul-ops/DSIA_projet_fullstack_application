from dotenv import dotenv_values
from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# import jwt
from jose import JWTError, jwt
from services import user as user_service
from models import db, models
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import secrets
from pydantic import BaseSettings
# hash = secrets.token_hex()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Settings(BaseSettings):


    # JWT  token
    ALGORITHM: str = "HS256"  # algo
    SECRET_KEY: str = secrets.token_urlsafe(32)  # random base64
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token expire in 3 days = 60 * 24 * 3


settings = Settings()


def get_hashed_password(password):
    return pwd_context.hash(password)


async def authenticate_user(username, passeword, db):
    user = user_service.get_post_by_username(username, db=db)
    if verify_password(passeword, user.password):
        return user
    return False


async def token_generator(username: str, password: str, db: Session = Depends(db.get_db)):
    user = await authenticate_user(username, password, db)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "nom d'utilisateur ou mot de passe incorrect.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {
        "id" : str(user.id),
        "email" : user.mail,
        'username' : user.username
    }

    # token = jwt.encode(token_data, settings.SECRET_KEY, algorithms=[
    #             settings.ALGORITHM])
    token = jwt.encode(token_data, "36a8ed70bd31a24543e6fb838fb23d9dd30a29ea", "HS256")
    
    return token


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



