from pydantic import BaseModel, Field
from typing_extensions import Annotated
from uuid import uuid4


class user_schema(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    username: str
    password: str
    mail: str

    class Config:
        orm_mode = True


class movies_schema(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    critic_reviews_num: float
    director_1: str
    director_2: str
    duration: str
    genres_1: str
    genres_2: str
    genres_3: str
    image: str
    metascore: float
    popularity: float
    presentation: str
    ranking_people: float
    rating: float
    reviews_num: float
    stars_1: str
    stars_2: str
    stars_3: str
    title: str
    url: str
    writers_1: str
    writers_2: str
    writers_3: str
    year: str

    class Config:
        orm_mode = True