from schemas.movies import Movie
from fastapi import status

from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

from services.movie import MovieService

def get_movies_fn() -> dict:
    try:
        db = Session()
        result_query = MovieService(db).get_movies()
        return {
            "content": jsonable_encoder(result_query),
            "status_code":status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }

def get_movies_by_id_fn(id: int) -> dict:
    try:
        db = Session()
        result_query = MovieService(db).get_movies_by_id(id)
        if not result_query:
            return {
                "content": {"message": f"Not found"}, 
                "status_code":status.HTTP_404_NOT_FOUND
            }    
        return {
            "content": jsonable_encoder(result_query),
            "status_code":status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }

def get_movies_by_category_fn(category: str) -> dict:
    try:
        db = Session()
        result_query = MovieService(db).get_movies_by_category_fn(category)
        if not result_query:
            return {
                "content": {"message": f"Not found"}, 
                "status_code":status.HTTP_404_NOT_FOUND
            }    
        return {
            "content": jsonable_encoder(result_query),
            "status_code":status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }

def create_movie_fn(new_movie: Movie) -> dict:
    try:
        db = Session()
        MovieService(db).create_movie(new_movie)
        return {
            "content": "movie created", 
            "status_code": status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }

def update_movie_fn(id, update_movie: Movie) -> dict:
    try: 
        db = Session()
        result_query = MovieService(db).get_movies_by_id(id)
        if not result_query:
            return {
                "content": {"message": f"Not found"}, 
                "status_code":status.HTTP_404_NOT_FOUND
            }
        MovieService(db).update_movie(id, update_movie)
        return {"content": "movie updated", "status_code": status.HTTP_200_OK}
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code": status.HTTP_400_BAD_REQUEST
        }

def delete_movie_fn(id: int) -> dict:
    try:
        db = Session()
        result_query = MovieService(db).get_movies_by_id(id)
        if not result_query:
            return {
                "content": {"message": f"Not found"}, 
                "status_code":status.HTTP_404_NOT_FOUND
            }
        MovieService.delete_movie(result_query)
        return {
            "content": "movie deleted",
            "status_code":status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }