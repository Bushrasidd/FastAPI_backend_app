from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name : str
    email: str
    password: str
    mobile_no :int

class UserResponse(BaseModel):
    name : str
    email: str
    mobile_no: int

class UpdateUser(BaseModel):
    name : Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    mobile_no :Optional[int] = None
