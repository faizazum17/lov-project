from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models.user_models import User, UserSchema, AnswerSchema
from fastapi import HTTPException, status
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from pydantic import EmailStr


def sign_up(request: UserSchema, db: Session):
    user = db.query(User).filter(User.email == request.email).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email sudah digunakan, gunakan email lain."
        )

    if len(request.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password paling tidak terdiri dari 8 karakter."
        )

    hashed_password = HashPassword().create_hash(request.password)
    new_user = User(email=request.email, nama=request.nama,
                    password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "Pesan": "Akun berhasil dibuat."
    }


def sign_in(request, db: Session):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Akun dengan email tersebut tidak ditemukan."
        )

    if not HashPassword().verify_hash(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Gagal, silahkan periksa email/password kembali!")

    access_token = create_access_token(user.email)

    return {"access_token": access_token, "token_type": "bearer"}


def get_all_user(db: Session):
    return db.query(User).all() 


def get_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User dengan id tersebut tidak ditemukan."
        )

    return user

def diagnose_love_language(request: AnswerSchema, db: Session, user: str):
    update_user = db.query(User).filter(User.email == user)

    kumpulan_jawaban = [request.jawaban_masalah_1, request.jawaban_masalah_2, request.jawaban_masalah_3, request.jawaban_masalah_4,
                        request.jawaban_masalah_5, request.jawaban_masalah_6, request.jawaban_masalah_7, request.jawaban_masalah_8, 
                        request.jawaban_masalah_9, request.jawaban_masalah_10]
    
    physical_touch = 0
    word_affirmation = 0
    gift = 0
    quality_time = 0
    act_of_service = 0

    for i in range(len(kumpulan_jawaban)):
        if i == 0:
            if kumpulan_jawaban[i] == 1:
                word_affirmation += 1
            elif kumpulan_jawaban[i] == 2:
                physical_touch += 1
            elif  kumpulan_jawaban[i] == 3:
                quality_time += 1
        elif i == 1:
            if  kumpulan_jawaban[i] == 1:
                act_of_service += 1
            elif kumpulan_jawaban[i] == 2:
                gift += 1
            elif kumpulan_jawaban[i] == 3:
                quality_time += 1
        elif i == 2:
            if kumpulan_jawaban[i] == 1:
                act_of_service += 1
            elif kumpulan_jawaban [i] == 2:
                physical_touch += 1
            elif kumpulan_jawaban [i] == 3:
                gift += 1
        elif i == 3:
            if kumpulan_jawaban [i] == 1:
                physical_touch += 1
            elif kumpulan_jawaban [i] == 2:
                quality_time += 1
            elif kumpulan_jawaban [i] == 3:
                word_affirmation += 1
        elif i == 4:
            if kumpulan_jawaban [i] == 1:
                gift += 1
            elif kumpulan_jawaban [i] == 2:
                word_affirmation += 1
            elif kumpulan_jawaban [i] == 3:
                act_of_service += 1
        elif i == 5:
            if kumpulan_jawaban [i] == 1:
                physical_touch += 1
            elif kumpulan_jawaban [i] == 2:
                quality_time += 1
            elif kumpulan_jawaban [i] == 3:
                gift += 1
        elif i == 6:
            if kumpulan_jawaban [i] == 1:
                act_of_service += 1
            elif kumpulan_jawaban [i] == 2:
                physical_touch += 1
            elif kumpulan_jawaban [i] == 3:
                word_affirmation += 1
        elif i == 7:
            if kumpulan_jawaban [i] == 1:
                gift += 1
            elif kumpulan_jawaban [i] == 2:
                quality_time += 1
            elif kumpulan_jawaban [i] == 3:
                physical_touch += 1
        elif i == 8:
            if kumpulan_jawaban [i] == 1:
                word_affirmation += 1
            elif kumpulan_jawaban [i] == 2:
                act_of_service += 1
            elif kumpulan_jawaban [i] == 3:
                gift += 1
        elif i == 9:
            if kumpulan_jawaban [i] == 1:
                act_of_service += 1
            elif kumpulan_jawaban [i] == 2:
                quality_time += 1
            elif kumpulan_jawaban [i] == 3:
                physical_touch += 1

    #cekJawabanQ1Q2 = kumpulan_jawaban[0] or kumpulan_jawaban[1]

    # kumpulan_lovlang = {physical_touch : "Physical Touch", 
    #                     word_affirmation : "Word of Affirmation", 
    #                     gift : "Gift", 
    #                     quality_time : "Quality Time", 
    #                     act_of_service : "Act of Service"}

    # Diagnosa
    # if kumpulan_lovlang.get(max(kumpulan_lovlang) == "a"):
    #     lovlang = "Physical Touch"
    # elif kumpulan_lovlang.get(max(kumpulan_lovlang) == "b"):
    #     lovlang = "Word of Affirmation"
    # elif kumpulan_lovlang.get(max(kumpulan_lovlang) == "c"):
    #     lovlang = "Gift"
    # elif kumpulan_lovlang.get(max(kumpulan_lovlang) == "d"):
    #     lovlang = "Quality Time"
    # else :
    #     lovlang = "Act of Service"
    a = (physical_touch / 10) * 100 
    b = (word_affirmation / 10) * 100 
    c = (gift / 10) * 100
    d = (quality_time / 10) * 100 
    e = (act_of_service / 10) * 100

    update_user.update({'physical_touch': a})
    update_user.update({'word_affirmation': b})
    update_user.update({'gift': c})
    update_user.update({'quality_time': d})
    update_user.update({'act_of_service': e})

    db.commit()

    return {"physical_touch": a, "word_affirmation": b, "gift": c, "quality_time": d, "act_of_service": e}