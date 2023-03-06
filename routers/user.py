from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.user import User
from services.fn_auth import login_fn

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def auth(user: User):
    response = login_fn(user)
    return JSONResponse(content=response['content'], status_code=response['status_code'])