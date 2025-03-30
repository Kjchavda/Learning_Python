from pydantic import BaseModel


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