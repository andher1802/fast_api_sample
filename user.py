from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    email:str = Field()
    password:str = Field()

