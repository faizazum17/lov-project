from auth.jwt_handler import verify_access_token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Silahkan sign in untuk mendapatkan akses."
        )

    decoded_token = await verify_access_token(token)
    return decoded_token["email"]
