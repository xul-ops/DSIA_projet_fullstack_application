from fastapi import APIRouter, Depends
import sys
sys.path.append("..")
from services import movie as movie_service
from models import db
from schemas import schemas
from sqlalchemy.orm import Session
import json

router = APIRouter(prefix="/movies")


# @router.post("/storeAllMovies", tags=["movies"])
# async def store_to_db(filename: str, db: Session = Depends(db.get_db)):
#     return posts_service.store_to_db(filename=filename, db=db)


@router.post("/importMovie", tags=["movies"])
async def import_movie(post: schemas.movies_schema, db: Session = Depends(db.get_db)):
    return movie_service.import_movie(post=post, db=db)


@router.get("/getMovieByTitle/{title}", tags=["movies"])
async def get_movie_by_title(title: str, db: Session = Depends(db.get_db)):
    return movie_service.get_movie_by_title(title=title, db=db)


@router.get("/getAllMovies", tags=["movies"])
async def get_all_movies(db: Session = Depends(db.get_db)):
    return movie_service.get_all_movies(db=db)


@router.get("/leaderBoard", tags=["movies"])
async def filter_movies(genre: str = "ALL", year: str = "ALL", rank: str = "rating", db: Session = Depends(db.get_db)):
    try:
        data = movie_service.filter_movies(genre=genre, year=year, rank=rank, db=db)
        data_return = dataProcessing(data)
        return {"code": 200, "data": data_return}
    except Exception as e:
        print("123")
        print(e)
        return {"code": 404, "data":[]}



@router.get("/movieSearchList", tags=["movies"])
async def get_movies_search_list(type: str = "Title", content: str = "", db: Session = Depends(db.get_db)):
    try:
        print(type, ":", content)
        if type == "Title":
            data = movie_service.get_movie_by_title(title=content, db=db)
            data_return = dataProcessing(data)
            return {"code": 200, "data": data_return}
        elif type == "Star":
            data = movie_service.get_movie_by_star(star=content, db=db)
            data_return = dataProcessing(data)
            return {"code": 200, "data": data_return}
        elif type == "Writer":
            data = movie_service.get_movie_by_writer(writer=content, db=db)
            data_return = dataProcessing(data)
            return {"code": 200, "data": data_return}
        elif type == "Director":
            data = movie_service.get_movie_by_director(director=content, db=db)
            data_return = dataProcessing(data)
            return {"code": 200, "data": data_return}
    except:

        return {"code": 404, "data": []}


@router.get("/getMovieById/{post_id}", tags=["movies"])
async def get_movie_by_id(post_id: str, db: Session = Depends(db.get_db)):
    print(post_id)
    try:
        data = movie_service.get_movie_by_id(post_id=post_id, db=db)
        return {"code": 200, "data": data}
    except:
        return {"code": 404, "data": []}


@router.put("/updateMovie/{post_id}", tags=["movies"])
async def update_movie_by_id(post_id: str, post: schemas.movies_schema,
                            db: Session = Depends(db.get_db)):
    return movie_service.update_movie(post_id=post_id, db=db, post=post)


@router.delete("/deleteMovie/{post_id}", tags=["movies"])
async def delete_movie(post_id: str, db: Session = Depends(db.get_db)):
    return movie_service.delete_movie(post_id=post_id, db=db)


def dataProcessing(data):

    data_return = []
    for item in data:
        star = []
        for s in [item.stars_1, item.stars_2, item.stars_3]:
            if s != "No_data":
                star.append(s)
        writer = []
        for w in [item.writers_1, item.writers_2, item.writers_3]:
            if w != "No_data":
                writer.append(w)
        director = []
        for d in [item.director_1, item.director_2]:
            if d != "No_data":
                director.append(d)
        genre = []
        for g in [item.genres_1, item.genres_2, item.genres_3]:
            if g != "No_data":
                genre.append(g)

        djson = {
            'id': item.id,
            'critic_reviews_num': item.critic_reviews_num,
            'director': director,
            'duration': item.duration,
            'category': item.genres_1,
            'genre': genre,
            'cover': item.image,
            'metaScore': item.metascore,
            'popularity': item.popularity,
            'presentation': item.presentation,
            'rankingPeople': item.ranking_people,
            'rating': float(item.rating),
            'reviewsNum': item.reviews_num,
            'star': star,
            'title': item.title,
            'url': item.url,
            'writer': writer,
            'year': item.year
        }
        data_return.append(djson)
    return data_return