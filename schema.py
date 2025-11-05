from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    email: str
    password: str
    mobile_no :int

class UserResponse(BaseModel):
    name : str
    email: str
    mobile_no: int