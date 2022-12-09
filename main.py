from fastapi import FastAPI
from database.db import engine
import uvicorn  
from models import user_models, question_models
#from apis.route_general_pages import general_pages_router
from apis.route_users import user_router
from apis.route_question import question_router
from apis.route_general_pages import general_pages_router

app = FastAPI()
app.debug  = True

user_models.Base.metadata.create_all(engine)
question_models.Base.metadata.create_all(engine)

app.include_router(user_router, prefix="/users")
app.include_router(question_router, prefix="/questions")
app.include_router(general_pages_router, prefix="/home")


@app.get('/')
def index():
    return {"Message" : "Hello, Welcome!"}

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="localhost", port=8000, reload=True)