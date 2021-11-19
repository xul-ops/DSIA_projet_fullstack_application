
from fastapi import APIRouter, Depends
import sys

from fastapi.params import Body
from sqlalchemy import and_

sys.path.append("..")
from services import user as user_service
from models import db, models
from schemas import schemas
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user")


@router.post("/inscription/", tags=["user"])
async def create_user(
        username: str = Body(..., embed=True),
        password1: str = Body(..., embed=True),
        email: str = Body(..., embed=True),
        db: Session = Depends(db.get_db)
):
    try:
        user_service.create_user(post={"username": username, "password": password1, "mail": email}, db=db)
        return {"code": 200, "message": "successful"}
    except:
        return {"code": 404, "message": "fail"}




@router.post("/login", tags=["user"])
async def login_user(
        username: str = Body(..., embed=True),
        password: str = Body(..., embed=True),
        db: Session = Depends(db.get_db)
):
    record = db.query(models.user_model).filter(and_(models.user_model.username == username, models.user_model.password == password)).first()
    if not record:
        return {"code": 404, "message": "error"}
    return {"code": 200, "message": "ok"}


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
