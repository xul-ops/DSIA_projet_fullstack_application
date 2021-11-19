import csv
from typing import List

import sqlalchemy
from sqlalchemy import or_, and_, desc
from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
sys.path.append("..")
from models import models
from schemas import schemas


def get_movie_by_title(title: str, db: Session) -> List[models.movie_model]:

    if title == "":
        return get_all_movies(db=db)
    else:
        records = db.query(models.movie_model).filter(
                            models.movie_model.title.like("%"+title+"%")
                ).order_by(desc(models.movie_model.rating)).all()
        if not records:
            raise HTTPException(status_code=404, detail="Not Found")
        return records


def get_movie_by_star(star: str, db: Session) -> List[models.movie_model]:

    if star == "":
        return get_all_movies(db=db)
    else:
        records = db.query(models.movie_model).filter(
            or_(
                models.movie_model.stars_1.like("%" + star + "%"),
                models.movie_model.stars_2.like("%" + star + "%"),
                models.movie_model.stars_3.like("%" + star + "%")
            )
        ).order_by(desc(models.movie_model.rating)).all()
        if not records:
            raise HTTPException(status_code=404, detail="Not Found")
        return records


def get_movie_by_writer(writer: str, db: Session) -> List[models.movie_model]:

    if writer == "":
        return get_all_movies(db=db)
    else:
        records = db.query(models.movie_model).filter(
            or_(
                models.movie_model.writers_1.like("%" + writer + "%"),
                models.movie_model.writers_2.like("%" + writer + "%"),
                models.movie_model.writers_3.like("%" + writer + "%")
            )
        ).order_by(desc(models.movie_model.rating)).all()
        if not records:
            raise HTTPException(status_code=404, detail="Not Found")
        return records


def get_movie_by_director(director: str, db: Session) -> List[models.movie_model]:

    if director == "":
        return get_all_movies(db=db)
    else:
        records = db.query(models.movie_model).filter(
            or_(
                models.movie_model.director_1.like("%" + director + "%"),
                models.movie_model.director_2.like("%" + director + "%")
            )
        ).order_by(desc(models.movie_model.rating)).all()
        if not records:
            raise HTTPException(status_code=404, detail="Not Found")
        return records


def import_movie(db: Session, post: schemas.movies_schema) -> models.movie_model:

    db_post = models.movie_model(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_all_movies(db: Session, skip: int = 0, limit: int = 20) -> List[models.movie_model]:

    records = db.query(models.movie_model).filter().order_by(desc(models.movie_model.rating)).offset(skip).limit(limit).all()
    for record in records:
        record.id = str(record.id)
    return records


def get_movie_by_id(post_id: str, db: Session) -> models.movie_model:

    record = db.query(models.movie_model).filter(models.movie_model.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


def update_movie(post_id: str, db: Session, post: schemas.movies_schema) -> models.movie_model:

    db_post = get_movie_by_id(post_id=post_id, db=db)
    for var, value in vars(post).items():
        setattr(db_post, var, value) if value else None
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_movie(post_id: str, db: Session) -> models.movie_model:

    db_post = get_movie_by_id(post_id=post_id, db=db)
    db.delete(db_post)
    db.commit()
    return db_post


def delete_all_movies(db: Session) -> List[models.movie_model]:

    records = db.query(models.movie_model).filter().order_by(models.movie_model.rating)
    for record in records:
        db.delete(record)
    db.commit()
    return records


def filter_movies(db: Session, genre, year, rank) -> List[models.movie_model]:

    if genre == "ALL" and year == "ALL" and rank == "rating":
        return get_all_movies(db=db)
    else:
        print(genre)
        if rank == "rating":
            if year == "ALL":
                records = db.query(models.movie_model).filter(
                                or_(
                                    models.movie_model.genres_1 == genre,
                                    models.movie_model.genres_2 == genre,
                                    models.movie_model.genres_3 == genre
                                )
                            ).order_by(desc(models.movie_model.rating)).limit(20).all()
            else:
                records = db.query(models.movie_model).filter(
                    and_(
                        or_(
                            models.movie_model.genres_1 == genre,
                            models.movie_model.genres_2 == genre,
                            models.movie_model.genres_3 == genre
                        ),
                        models.movie_model.year == year
                    )
                ).order_by(desc(models.movie_model.rating)).limit(20).all()

        elif rank == "popularity":
            if year == "ALL":
                records = db.query(models.movie_model).filter(
                    or_(
                        models.movie_model.genres_1 == genre,
                        models.movie_model.genres_2 == genre,
                        models.movie_model.genres_3 == genre
                    )
                ).order_by(desc(models.movie_model.popularity)).limit(20).all()
            else:
                records = db.query(models.movie_model).filter(
                    and_(
                        or_(
                            models.movie_model.genres_1 == genre,
                            models.movie_model.genres_2 == genre,
                            models.movie_model.genres_3 == genre
                        ),
                        models.movie_model.year == year
                    )
                ).order_by(desc(models.movie_model.popularity)).limit(20).all()

        elif rank == "metascore":
            if year == "ALL":
                records = db.query(models.movie_model).filter(
                    or_(
                        models.movie_model.genres_1 == genre,
                        models.movie_model.genres_2 == genre,
                        models.movie_model.genres_3 == genre
                    )
                ).order_by(desc(models.movie_model.metascore)).limit(20).all()
            else:
                records = db.query(models.movie_model).filter(
                    and_(
                        or_(
                            models.movie_model.genres_1 == genre,
                            models.movie_model.genres_2 == genre,
                            models.movie_model.genres_3 == genre
                        ),
                        models.movie_model.year == year
                    )
                ).order_by(desc(models.movie_model.metascore)).limit(20).all()

        elif rank == "ranking_people":
            if year == "ALL":
                records = db.query(models.movie_model).filter(
                    or_(
                        models.movie_model.genres_1 == genre,
                        models.movie_model.genres_2 == genre,
                        models.movie_model.genres_3 == genre
                    )
                ).order_by(desc(models.movie_model.ranking_people)).limit(20).all()
            else:
                records = db.query(models.movie_model).filter(
                    and_(
                        or_(
                            models.movie_model.genres_1 == genre,
                            models.movie_model.genres_2 == genre,
                            models.movie_model.genres_3 == genre
                        ),
                        models.movie_model.year == year
                    )
                ).order_by(desc(models.movie_model.ranking_people)).limit(20).all()

        return records


def store_to_db(db: Session, filename: str):

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        cnt = 0
        for line in reader:
            record = models.movie_model(**{
                'critic_reviews_num': line[0],
                'director_1': line[1],
                'director_2': line[2],
                'duration': line[3],
                'genres_1': line[4],
                'genres_2': line[5],
                'genres_3': line[6],
                'image': line[7],
                'metascore': line[8],
                'popularity': line[9],
                'presentation': line[10],
                'ranking_people': line[11],
                'rating': line[12],
                'reviews_num': line[13],
                'stars_1': line[14],
                'stars_2': line[15],
                'stars_3': line[16],
                'title': line[17],
                'url': line[18],
                'writers_1': line[19],
                'writers_2': line[20],
                'writers_3': line[21],
                'year': line[22]
            })

            try:
                db.add(record)
                cnt += 1
                if cnt % 1000 == 0:
                    db.commit()
            except sqlalchemy.exc.PendingRollbackError:
                db.rollback()
                db.add(record)
            except Exception as e:
                print(e)
                break
    db.commit()
    return record
