from fastapi import FastAPI, Depends
from keycloak import KeycloakOpenID
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

# psql -U userpd -W dbesiee(database name), then enter password
# \dt : show all tables
# TABLE tablename(or select * from tablename) : show all records of table
from models.database import BaseSQL, engine, SessionLocal
from models import models
from routers import user, movie
from services import movie as movie_service

app = FastAPI()





# front url
origins = [
    "http://localhost",
    "http://localhost:5050",
    "http://localhost:5050/#/movie/list",
    "http://localhost:5050/#/movie/search",
    "http://localhost:5050/#/",
]

# fastapi allow cross-domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World_first"}


app.include_router(user.router)
app.include_router(movie.router)


@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        db.query(models.movie_model).delete()
        db.commit()
    except:
        db.rollback()
    movie_service.store_to_db(db=db, filename='imdb_movies.csv')


# # authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# # Configure client
# keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
#                                  client_id="fastapi",
#                                  realm_name="master",
#                                  client_secret_key="be49e1f0-922d-4c06-8f61-d5ad3a46f896")
#
#
# @app.get("/protected", tags=["authentication"])
# def protected(token: str = Depends(oauth2_scheme)):
#     return {
#         "Hello": "World",
#         "user_infos": token
#     }

