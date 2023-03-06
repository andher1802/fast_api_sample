from fastapi.security import HTTPBearer
from fastapi import status, Request, HTTPException
from services.fn_auth import authenticate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = authenticate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, content="invalid credentials")