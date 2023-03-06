from fastapi import FastAPI, Query, status, Depends
from fastapi.responses import HTMLResponse, JSONResponse

from movies import Movie, movies
from user import User
from fn_movies import *
from fn_auth import login_fn

from typing import List
from config.database import Base, engine

from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer

app = FastAPI()
app.title = "Test application"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies() ->  dict:
    response = get_movies_fn()
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@app.get('/movies/{id}', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movie(id: int)  -> dict:
    response = get_movies_by_id_fn(id)
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@app.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15), year: int = Query(le=2022)) -> dict:
    response = get_movies_by_category_fn(category)
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@app.post('/movies', tags=["movies"], response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
async def create_movie(movie: Movie) -> dict:
    response = create_movie_fn(movies, {
        "title":movie.title,
        "overview":movie.overview,
        "year":movie.year,
        "rating":movie.rating,
        "category":movie.category,
    })
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@app.put('/movies', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
async def update_movie(id: int, movie: Movie) -> dict:
    response = update_movie_fn(
        movies,
        id, 
        {
            "title":movie.title,
            "overview":movie.overview,
            "year":movie.year,
            "rating":movie.rating,
            "category":movie.category
        }
        )
    return JSONResponse(content=response['content'], status_code=response['status_code'])
    
@app.delete('/movies', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
async def delete_movie(id: int) -> dict:
    response = delete_movie_fn(id)
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@app.post('/login', tags=['auth'])
def auth(user: User):
    response = login_fn(user)
    return JSONResponse(content=response['content'], status_code=response['status_code'])