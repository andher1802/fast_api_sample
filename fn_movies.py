from movies import Movie
from fastapi import status

from config.database import Session, engine
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

def get_movies_fn() -> dict:
    try:
        db = Session()
        result_query = db.query(MovieModel).all()
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
        result_query = db.query(MovieModel).filter(MovieModel.id==id).first()
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
        result_query = db.query(MovieModel).filter(MovieModel.category==category).all()
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

def create_movie_fn(movies: list[Movie], new_movie: Movie) -> dict:
    try:
        db = Session()
        movie_model_instance = MovieModel(**new_movie)
        db.add(movie_model_instance)
        db.commit()
        return {
            "content": "movie created", 
            "status_code": status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }

def update_movie_fn(movies: list[Movie], id, update_movie: Movie) -> dict:
    try: 
        db = Session()
        result_query = db.query(MovieModel).filter(MovieModel.id==id).first()
        if not result_query:
            return {
                "content": {"message": f"Not found"}, 
                "status_code":status.HTTP_404_NOT_FOUND
            }
        result_query.title = update_movie['title']
        result_query.overview = update_movie['overview']
        result_query.year = update_movie['year']
        result_query.rating = update_movie['rating']
        result_query.category = update_movie['category']
        db.commit()
        return {"content": "movie updated", "status_code": status.HTTP_200_OK}
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code": status.HTTP_400_BAD_REQUEST
        }

def delete_movie_fn(id: int) -> dict:
    try:
        db = Session()
        result_query = db.query(MovieModel).filter(MovieModel.id==id).first()
        if not result_query:
            return {
                "content": {"message": f"Not found"}, 
                "status_code":status.HTTP_404_NOT_FOUND
            }
        db.delete(result_query)
        db.commit()
        return {
            "content": "movie deleted",
            "status_code":status.HTTP_200_OK
        }
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code":status.HTTP_400_BAD_REQUEST
        }