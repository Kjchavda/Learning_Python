from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostResponse(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Token_data(BaseModel):
    id:Optional[str]
    