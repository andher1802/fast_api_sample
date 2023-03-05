from movies import Movie
from fastapi import status

def create_movie_fn(movies: list[Movie], new_movie: Movie) -> dict:
    try:
        movies.append(new_movie)
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
    updated = False
    try: 
        for index, movie in enumerate(movies):
            if id == movie['id']:
                updated = True
                movies[index].update(update_movie)
        return {"content": "movie updated", "status_code": status.HTTP_200_OK} if updated else {"content": "movie not found", "status_code": status.HTTP_404_NOT_FOUND}
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code": status.HTTP_400_BAD_REQUEST
        }

def delete_movie_fn(movies: list[Movie], id: int) -> dict:
    try:
        movies_original_length = len(movies)
        movies_filtered = [movie for movie in movies if movie['id'] != id]
        movies[:] = movies_filtered[:]
        return {"content": "movie deleted", "status_code": status.HTTP_200_OK} if len(movies) != movies_original_length else {"content": "movie not found", "status_code": status.HTTP_404_NOT_FOUND}
    except Exception as e:
        return {
            "content": f"Something went wrong with error {e}", 
            "status_code": status.HTTP_400_BAD_REQUEST
        }