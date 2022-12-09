from database.db import get_db
from fastapi import APIRouter, Depends
from models.attachmentstyle_models import *
# from models.userModels import ShowUser
from sqlalchemy.orm import Session
from typing import List
from auth.authenticate import authenticate
from pydantic import EmailStr, HttpUrl

from controllers import attachmentstyle_controllers

attachmentstyle_router = APIRouter(
    tags=["Attachment Style"],
)

@attachmentstyle_router.put("/users")
def get_user_list(request: UserAttachmentRequest, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return attachmentstyle_controllers.get_love_attachment(request, db, user)