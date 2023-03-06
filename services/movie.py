from models.movie import Movie
from models.movie import Movie as MovieModel
from typing import List

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self) -> List[Movie]:
        result_query = self.db.query(MovieModel).all()
        return result_query

    def get_movies_by_id(self, id: int) -> Movie:
        result_query = self.db.query(MovieModel).filter(MovieModel.id==id).first()
        return result_query
    
    def get_movies_by_category(self, category: str) -> List[Movie]:
        result_query = self.db.query(MovieModel).filter(MovieModel.category==category).all()
        return result_query
    
    def create_movie(self, new_movie: Movie) -> None:
        movie_model_instance = MovieModel(**new_movie)
        self.db.add(movie_model_instance)
        self.db.commit()
        return
    
    def update_movie(self, id, new_movie: Movie) -> None:
        result_query = self.get_movies_by_id(id)
        result_query.title = new_movie['title']
        result_query.overview = new_movie['overview']
        result_query.year = new_movie['year']
        result_query.rating = new_movie['rating']
        result_query.category = new_movie['category']
        self.db.commit()
        return
    
    def delete_movie(self, result_query) -> None:
        self.db.delete(result_query)
        self.db.commit()
        return