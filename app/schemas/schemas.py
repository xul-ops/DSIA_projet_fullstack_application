from pydantic import BaseModel, Field
from typing_extensions import Annotated
from uuid import uuid4
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


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



class CodeEnum(int, Enum):
    """code"""
    SUCCESS = 200
    FAIL = 400


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="code 200 is success, 400 failed")
    data: Any = Field(default=None, description="data")
    msg: str = Field(default="successful", description="Tip")


class Response200(ResponseBasic):
    pass


class ResponseToken(Response200):
    access_token: str
    token_type: str = Field(default="bearer")


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = "failed"