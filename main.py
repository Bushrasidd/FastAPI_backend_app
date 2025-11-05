from fastapi import FastAPI, Depends, HTTPException, status,Query 
from models import User
from database import engine
from dependency import get_db
from pydantic import BaseModel
from schema import *
from sqlalchemy.exc import IntegrityError,SQLAlchemyError

app = FastAPI()

@app.get("/")
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
    if filter_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "The user equivalent to given id does not exist"
        )
    else:
        return [filter_user]
    
    users = db.query(   User).all()
    return users

@app.patch("/user/update/{user_id}", status_code = status.HTTP_200_OK)
def update_user(user_id:int,user:UpdateUser,db = Depends(get_db)):
    q = db.query(User).filter(User.id == user_id).first()
    if not q:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user equivalent to given id does not exist"
        )
    update_user = user.dict(exclude_unset=True)
                            
    try:
        for key, value in update_user.items():
            setattr(q, key, value)
        db.commit()
        db.refresh(update_user)
        return{"status": "success", "data": q}
    except IntegrityError as e :
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "user with this unique field already exist"
        )from e
    return{"error" : e}
    



