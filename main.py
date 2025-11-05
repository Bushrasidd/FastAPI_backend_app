from fastapi import FastAPI, Depends, HTTPException, status
from models import User
from database import engine
from dependency import get_db
from pydantic import BaseModel
from schema import UserCreate

app = FastAPI()

@app.get("/")
def greetings():
    return ("Hello Bushra you finally started writing code, just keep trying you will make it one day inshallah")

@app.post("/user/")
async def create_user(user : UserCreate, db = Depends(get_db)):
    user_data = User(**user.dict())
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    print(user_data)
    return user_data
