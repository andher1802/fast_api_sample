from fastapi import APIRouter
from fastapi import Query, status, Depends
from fastapi.responses import JSONResponse

from schemas.movies import Movie
from services.fn_movies import *

from typing import List
from middlewares.jwt_bearer import JWTBearer

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies() ->  dict:
    response = get_movies_fn()
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@movie_router.get('/movies/{id}', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movie(id: int)  -> dict:
    response = get_movies_by_id_fn(id)
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15), year: int = Query(le=2022)) -> dict:
    response = get_movies_by_category_fn(category)
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@movie_router.post('/movies', tags=["movies"], response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
async def create_movie(movie: Movie) -> dict:
    response = create_movie_fn({
        "title":movie.title,
        "overview":movie.overview,
        "year":movie.year,
        "rating":movie.rating,
        "category":movie.category,
    })
    return JSONResponse(content=response['content'], status_code=response['status_code'])

@movie_router.put('/movies', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
async def update_movie(id: int, movie: Movie) -> dict:
    response = update_movie_fn(
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
    
@movie_router.delete('/movies', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
async def delete_movie(id: int) -> dict:
    response = delete_movie_fn(id)
    return JSONResponse(content=response['content'], status_code=response['status_code'])
