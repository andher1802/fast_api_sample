from fastapi import status

from user import User
from jwt_manager import create_token, validate_token

def login_fn(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict())
        return {
            "content": token, 
            "status_code": status.HTTP_200_OK
        }
    return {
            "content": None, 
            "status_code": status.HTTP_401_UNAUTHORIZED
        }

def authenticate_token (credentials: str):
    return validate_token(credentials)
