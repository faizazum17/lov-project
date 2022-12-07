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
    healthiness = Column(String, default="")

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
    healthiness : str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@mail.com",
                "nama": "Yanto",
                "healthiness": "Greenlight",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class AnswerSchema(BaseModel):
    jawaban_masalah_1: conint(gt=-1, lt=4)
    jawaban_masalah_2: conint(gt=-1, lt=4)
    jawaban_masalah_3: conint(gt=-1, lt=4)
    jawaban_masalah_4: conint(gt=-1, lt=4)
    jawaban_masalah_5: conint(gt=-1, lt=4)
    jawaban_masalah_6: conint(gt=-1, lt=4)
    jawaban_masalah_7: conint(gt=-1, lt=4)
    jawaban_masalah_8: conint(gt=-1, lt=4)
    jawaban_masalah_9: conint(gt=-1, lt=4)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "jawaban_pertanyaan_1": 0,
                "jawaban_pertanyaan_2": 1,
                "jawaban_pertanyaan_3": 0,
                "jawaban_pertanyaan_4": 2,
                "jawaban_pertanyaan_5": 0,
                "jawaban_pertanyaan_6": 3,
                "jawaban_pertanyaan_7": 0,
                "jawaban_pertanyaan_8": 1,
                "jawaban_pertanyaan_9": 2

            }
        }
