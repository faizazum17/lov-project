import time
from datetime import datetime, timedelta

from database.db import Settings
from fastapi import HTTPException, status
from jose import jwt, JWTError
from models.user_models import TokenData


settings = Settings()


def create_access_token(email: str) -> str:
    payload = {
        "email": email,
        "expires": time.time() + 3600
    }

    token = jwt.encode(payload, settings.SECRET_KEY,
                       algorithm=settings.ALGORTIM)
    return token


async def verify_access_token(token: str) -> dict:
    try:
        data = jwt.decode(token, settings.SECRET_KEY,
                          algorithms=settings.ALGORTIM)
        email: str = data.get("email")
        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token kadaluarsa!"
            )

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token tidak valid!"
            )

        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token tidak valid!"
        )
