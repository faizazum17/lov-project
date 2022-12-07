from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel, EmailStr, conint
from typing import Optional


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    nama = Column(String)
    password = Column(String)
    physical_touch = Column(Integer, default=0)
    word_affirmation = Column(Integer, default=0)
    gift = Column(Integer, default=0)
    quality_time = Column(Integer, default=0)
    act_of_service = Column(Integer, default=0)
    
    class Config:
        schema_extra = {
            "Contoh": {
                "email": "example@mail.com",
                "nama": "Yanto",
                "password": "1234",
            }
        }


class UserSchema(BaseModel):
    email: EmailStr
    nama: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@mail.com",
                "nama": "Yanto",
                "password": "1234",
            }
        }


class ShowUser(BaseModel):
    email: EmailStr
    nama: str
    physical_touch : int
    word_affirmation : int
    gift : int
    quality_time : int
    act_of_service : int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@mail.com",
                "nama": "Yanto",
                "phyisical_touch (%)" : "20",
                "word_affirmation (%)" : "20",
                "gif (%)" : "20",
                "quality_time (%)" : "20",
                "act_of_service (%)" : "20",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class AnswerSchema(BaseModel):
    jawaban_masalah_1: conint(gt=-0, lt=4)
    jawaban_masalah_2: conint(gt=-0, lt=4)
    jawaban_masalah_3: conint(gt=-0, lt=4)
    jawaban_masalah_4: conint(gt=-0, lt=4)
    jawaban_masalah_5: conint(gt=-0, lt=4)
    jawaban_masalah_6: conint(gt=-1, lt=4)
    jawaban_masalah_7: conint(gt=-1, lt=4)
    jawaban_masalah_8: conint(gt=-1, lt=4)
    jawaban_masalah_9: conint(gt=-1, lt=4)
    jawaban_masalah_10: conint(gt=-1, lt=4)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "jawaban_masalah_1": 1,
                "jawaban_masalah_2": 1,
                "jawaban_masalah_3": 2,
                "jawaban_masalah_4": 2,
                "jawaban_masalah_5": 3,
                "jawaban_masalah_6": 1,
                "jawaban_masalah_7": 2,
                "jawaban_masalah_8": 3, 
                "jawaban_masalah_9": 1,
                "jawaban_masalah_10": 2
            }
        }
