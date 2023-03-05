from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(
        min_length=5,
        max_length=15,
    )
    overview: str = Field(
        min_length=50,
        max_length=150,
    )
    year: int = Field(
        le = 2022,
    )
    rating: float
    category: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title":"movie's title",
                "overview":"",
                "year":2022,
                "rating":5,
                "category":"general"
            } 
        }

movies:list[Movie] = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "Lorem ipsum",
        "year": 2010,
        "rating": 7.8,
        "category": "Action"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "Lorem ipsum",
        "year": 2010,
        "rating": 7.8,
        "category": "Action"
    },
]