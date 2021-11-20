
from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import sys
sys.path.append("..")
from models import models
from schemas import schemas


def create_user(db: Session, post) -> models.user_model:

    db_post = models.user_model(**post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post_by_mail(mail: str, db: Session) -> models.user_model:

    record = db.query(models.user_model).filter(models.user_model.mail == mail).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


def get_post_by_username(username: str, db: Session) -> models.user_model:

    record = db.query(models.user_model).filter(models.user_model.username == username).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


def get_all_users(db: Session, skip: int = 0, limit: int = 10) -> List[models.user_model]:

    records = db.query(models.user_model).filter().offset(skip).limit(limit).all()
    for record in records:
        record.id = str(record.id)
    return records


def get_user_by_id(post_id: str, db: Session) -> models.user_model:

    record = db.query(models.user_model).filter(models.user_model.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


def update_user(post_id: str, db: Session, post: schemas.user_schema) -> models.user_model:

    db_post = get_user_by_id(post_id=post_id, db=db)
    for var, value in vars(post).items():
        setattr(db_post, var, value) if value else None
    db_post.updated_at = datetime.now()
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_user(post_id: str, db: Session) -> models.user_model:

    db_post = get_user_by_id(post_id=post_id, db=db)
    db.delete(db_post)
    db.commit()
    return db_post


def delete_all_users(db: Session) -> List[models.user_model]:

    records = db.query(models.user_model).filter()
    for record in records:
        db.delete(record)
    db.commit()
    return records