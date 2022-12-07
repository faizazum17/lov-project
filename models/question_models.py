from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    masalah = Column(String)
    pilihan = Column(String)

    class Config:
        schema_extra = {
            "Contoh": {
                "pertanyaan": "Pasanganku memandang perilaku serta perkataanku secara negatif. ",
                "pilihan": "1 (Hampir Tidak Pernah), 2 (Terkadang), 3 (Sering)"
            }
        }


class QuestionSchema(BaseModel):
    masalah: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pertanyaan": "Pasanganku memandang perilaku serta perkataanku secara negatif. ",
                "pilihan": "1 (Hampir Tidak Pernah), 2 (Terkadang), 3 (Sering)"
            }
        }


class QuestionShow(BaseModel):
    id: int
    masalah: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "int": 1,
                "pertanyaan": "Pasanganku memandang perilaku serta perkataanku secara negatif. ",
                "pilihan": "1 (Hampir Tidak Pernah), 2 (Terkadang), 3 (Sering)"
            }
        }


class QuestionUpdate(BaseModel):
    masalah: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pertanyaan": "Pasanganku memandang perilaku serta perkataanku secara negatif. ",
            }
        }

