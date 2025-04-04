from fastapi import Depends, FastAPI, HTTPException, Response, status
import psycopg2.extras
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
import models
from database import engine, get_db
import schemas 
import utils
import post, user, auth

models.Base.metadata.create_all(bind=engine)
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

try:
    conn = psycopg2.connect(host="localhost", database="Learn_FastAPI", user="postgres", password="kj0910", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("success")

except Exception as error:
    print("failed")
    print("Error:" , error)


my_posts = [{"title": "title1", "content": "content1", "id":1}, {"title": "fav food", "content": "pizza", "id":2}]

app.include_router(post.router)

app.include_router(user.router)

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my API"} 

