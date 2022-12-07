from database.db import get_db
from fastapi import APIRouter, Depends
from models.question_models import QuestionSchema, QuestionUpdate, QuestionShow
from models.user_models import UserSchema
from sqlalchemy.orm import Session
from typing import List
from auth.authenticate import authenticate


from controllers import question_controllers

question_router = APIRouter(
    tags=["Question"],
)


@question_router.post("/create")
def create_a_question(request: QuestionSchema, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return question_controllers.create_quesiton(request, db, user)


@question_router.get("/", response_model=List[QuestionShow])
def get_all_questions(db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return question_controllers.get_questions(db)


@question_router.get("/{id}", response_model=QuestionShow)
def get_a_question(id: int, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return question_controllers.get_question(id, db)


@question_router.put("/update/{id}")
def update_a_question(id: int, request: QuestionUpdate, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return question_controllers.update_question(id, request, db, user)


@question_router.delete("/delete/{id}")
def delete_a_question(id: int, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return question_controllers.delete_question(id, db, user)

