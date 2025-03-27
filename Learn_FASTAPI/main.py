from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

my_posts = []

@app.get("/")
async def root():
    return {"message": "Welcome to my API"} 

@app.get("/posts")
def get_posts():
    return {"data": "here are all the posts"}

@app.post("/posts")
def create_post(post: Post):
    print(post.dict())
    return {"msg": "Succesfully created"}
