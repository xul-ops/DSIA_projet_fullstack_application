from uuid import uuid4

from fastapi import APIRouter, Depends, FastAPI
import sys

from fastapi.params import Body
from sqlalchemy import and_
from .authentification import *

sys.path.append("..")
from services import user as user_service
from models import db, models
from schemas import schemas
from sqlalchemy.orm import Session
from dotenv import dotenv_values
from passlib.context import CryptContext
from fastapi import HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(prefix="/user")
login = APIRouter(tags=["authN"])


@router.post("/inscription/", tags=["user"])
async def create_user(
        username: str = Body(..., embed=True),
        password1: str = Body(..., embed=True),
        email: str = Body(..., embed=True),
        db: Session = Depends(db.get_db)
):
    try:
        password1 = get_hashed_password(password1)
        user_service.create_user(post={"username": username, "password": password1, "mail": email}, db=db)
        return {"code": 200, "message": "successful"}
    except:
        return {"code": 404, "message": "fail"}


# @router.post("/login", tags=["user"])
# async def login_user(
#         # post: schemas.user_schema,
#         username: str = Body(..., embed=True),
#         password: str = Body(..., embed=True),
#         db: Session = Depends(db.get_db)
# ):
#     record = db.query(models.user_model).filter(and_(models.user_model.username == username, models.user_
#     model.password == password)).first()
#     if not record:
#         return {"code":205, "message":"error"}
#     return {"code":200,"message":"ok"}


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='user/login')


@router.post("/login")
async def login_for_access_token(request_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
    token = await token_generator(request_form.username, request_form.password, db)
    # print(token)

    return schemas.ResponseToken(data={"token": f"bearer {token}"}, access_token=token)


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.get_db)):
    try:
        payload = jwt.decode(token_data, "36a8ed70bd31a24543e6fb838fb23d9dd30a29ea", "HS256")
        # payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user = user_service.get_post_by_username(payload['username'], db=db)
    except:
        raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = token,
                headers={"WWW-Authenticate": "Bearer"},)
    return user


@router.post('/user/me/', tags=["user"])
async def user_me(user: schemas.user_schema = Depends(get_current_user)):

    return {
        "status" : "ok",
        "data" : {
                "nom d'user" : user.username,
                "email" : user.mail,
        }}


@router.get("/getUser/{post_id}", tags=["user"])
async def get_post_by_id(post_id: str, db: Session = Depends(db.get_db)):
    return user_service.get_user_by_id(post_id=post_id, db=db)


@router.get("/getAllUsers", tags=["user"])
async def get_all_users(db: Session = Depends(db.get_db)):
    return user_service.get_all_users(db=db)


@router.put("/updateUser/{post_id}", tags=["user"])
async def update_post_by_id(post_id: str, post: schemas.user_schema,
                            db: Session = Depends(db.get_db)):
    return user_service.update_user(post_id=post_id, db=db, post=post)


@router.delete("/deleteUser/{post_id}", tags=["user"])
async def delete_post_by_id(post_id: str, db: Session = Depends(db.get_db)):
    return user_service.delete_user(post_id=post_id, db=db)
