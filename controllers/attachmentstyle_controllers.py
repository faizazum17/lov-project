from sqlalchemy.orm import Session
from models.attachmentstyle_models import ShowUserAttachment, UserAttachmentRequest
from models.user_models import User
from fastapi import HTTPException, status
import requests

#callback_url = "https://lovelangapi.politeground-4e0e77af.eastus.azurecontainerapps.io/"
callback_url = "https://apiadit.calmpond-d268450b.eastus.azurecontainerapps.io/"

def get_love_attachment(request: UserAttachmentRequest, db: Session, user: str):
    # signup = requests.post(callback_url + "users/signup", json= {
    #     "email": request.username,
    #     "nama": "Adit",
    #     "password": request.password,
    # })
    db_user = db.query(User).filter(User.email == user).first()
 
    res = requests.post(callback_url +"users/signin", data= {
        "username": request.username, 
        "password": request.password,})
    
    session = requests.Session()
    out = session.get(callback_url + "users/", 
        headers={"Authorization": "Bearer " + res.json().get("access_token")})
    
    for row in out.json():
        if row.get("email") == request.username:
            userOut = ShowUserAttachment(
                nama= db_user.nama, 
                physical_touch= db_user.physical_touch,
                word_affirmation= db_user.word_affirmation,
                receiving_gift= db_user.gift,
                quality_time= db_user.quality_time,
                act_of_service= db_user.act_of_service,
                attachment= row.get("attachment"),
            )
            return userOut