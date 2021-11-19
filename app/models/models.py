from .database import BaseSQL
from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class user_model(BaseSQL):

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=lambda: uuid4().hex)
    username = Column(String)
    password = Column(String)
    mail = Column(String)


class movie_model(BaseSQL):

    __tablename__ = "movies"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=lambda: uuid4().hex)
    critic_reviews_num = Column(Float)
    director_1 = Column(String)
    director_2 = Column(String)
    duration = Column(String)
    genres_1 = Column(String)
    genres_2 = Column(String)
    genres_3 = Column(String)
    image = Column(String)
    metascore = Column(Float)
    popularity = Column(Float)
    presentation = Column(String)
    ranking_people = Column(Float)
    rating = Column(Float)
    reviews_num = Column(Float)
    stars_1 = Column(String)
    stars_2 = Column(String)
    stars_3 = Column(String)
    title = Column(String)
    url = Column(String)
    writers_1 = Column(String)
    writers_2 = Column(String)
    writers_3 = Column(String)
    year = Column(String)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result