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
            "Example": {
                "pertanyaan": "Aku merasa lebih dicintai ketika... ",
                "pilihan": "Seorang yang kucinta mengirimkan pesan tanpa sebab khusus(1), Aku memeluk orang yang kucintai (2), Menghabiskan waktu berdua saja(3) "
            }
        }


class QuestionSchema(BaseModel):
    masalah: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "Example": {
                "pertanyaan": "Aku merasa lebih dicintai ketika... ",
                "pilihan": "Seorang yang kucinta mengirimkan pesan tanpa sebab khusus(1), Aku memeluk orang yang kucintai (2), Menghabiskan waktu berdua saja(3) "
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
                "pertanyaan": "Aku merasa lebih dicintai ketika... ",
                "pilihan": "Seorang yang kucinta mengirimkan pesan tanpa sebab khusus(1), Aku memeluk orang yang kucintai (2), Menghabiskan waktu berdua saja(3) "
            }
        }


class QuestionUpdate(BaseModel):
    masalah: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "int": 1,
                "pertanyaan": "Aku merasa lebih dicintai ketika... ",
                "pilihan": "Seorang yang kucinta mengirimkan pesan tanpa sebab khusus(1), Aku memeluk orang yang kucintai (2), Menghabiskan waktu berdua saja(3) "
            }
        }

