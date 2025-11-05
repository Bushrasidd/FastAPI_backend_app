from fastapi import FastAPI, Depends, HTTPException, status,Query 
from models import User
from database import engine
from dependency import get_db
from pydantic import BaseModel
from schema import *

app = FastAPI()

@app.get("/user/greetings")
def greetings():
    return ("Hello Bushra you finally started writing code, just keep trying you will make it one day inshallah")

@app.post("/user/create_user",status_code=status.HTTP_201_CREATED)
async def create_user(user : UserCreate, db = Depends(get_db)):
    user_data = User(**user.dict())
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = "User with this already exist" 
        )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return { "status": "success", "data": user_data }

@app.get("/user/Get_all_users",response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(id:int = Query(None), db = Depends(get_db)):
    if id:
        filter_user = db.query(User).filter(User.id == id).first()
        return [filter_user]
    users = db.query(   User).all()
    return users

