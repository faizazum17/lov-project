from sqlalchemy.orm import Session
from models.question_models import QuestionSchema, Question, QuestionUpdate
from fastapi import HTTPException, status

def create_quesiton(request: QuestionSchema, db: Session, user:str):
    if (user != "admin@gmail.com"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Fitur ini hanya dapat digunakan oleh admin."
        )

    masalah = db.query(Question).filter(Question.masalah == request.masalah)

    if masalah.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Pertanyaan tersebut sudah ada."
        )

    masalah_baru = Question(masalah=request.masalah, pilihan=request.pilihan)
    db.add(masalah_baru)
    db.commit()
    db.refresh(masalah_baru)

    return {
        "Pesan": "Pertanyaan berhasil ditambahkan."
    }

def get_questions(db: Session):
    return db.query(Question).all()


def get_question(id: int, db: Session):
    masalah = db.query(Question).filter(Question.id == id)

    if not masalah.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Pertanyaan dengan id tersebut tidak ditemukan."
        )

    return masalah.first()


def update_question(id: int, request: QuestionUpdate, db: Session, user:str):
    if (user != "admin@gmail.com"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Fitur ini hanya dapat digunakan oleh admin."
        )

    masalah = db.query(Question).filter(Question.id == id)

    if not masalah.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pertanyaan dengan id tersebut tidak ditemukan."
        )

    masalah.update({'Pertanyaan': request.masalah})
    masalah.update({'pilihan': request.pilihan})
    db.commit()

    return {
        "Pesan": "Pertanyaan berhasil diperbarui."
    }


def delete_question(id: int, db: Session, user:str):
    if (user != "admin@gmail.com"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Fitur ini hanya dapat digunakan oleh admin."
        )

    masalah = db.query(Question).filter(Question.id == id)

    if not masalah.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pertanyaan dengan id tersebut tidak ditemukan."
        )

    masalah.delete(synchronize_session=False)
    db.commit()

    return {
        "Pesan": "Masalah berhasil dihapus."
    }

