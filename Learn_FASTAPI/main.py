from fastapi import FastAPI, HTTPException, Response, status
import psycopg2.extras
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    
    published: bool = True

try:
    conn = psycopg2.connect(host="localhost", database="Learn_FastAPI", user="postgres", password="kj0910", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("success")

except Exception as error:
    print("failed")
    print("Error:" , error)


my_posts = [{"title": "title1", "content": "content1", "id":1}, {"title": "fav food", "content": "pizza", "id":2}]

@app.get("/")
async def root():
    return {"message": "Welcome to my API"} 

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)    #status code parameter to select default status code
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i 

@app.get("/posts/{id}")
def get_post(id: int, response: Response): #No need to pass in response now
    """
        post = find_post(id)
    if not post:
            #Below code is a sloppy way to implement HTTP error
            # response.status_code = status.HTTP_404_NOT_FOUND    #can also be hardcode to 404
            # return {"msg": f"post with id {id} was not found"}
            # a better way to do this will be the following, raising HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    """
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()

    if not post:
            #Below code is a sloppy way to implement HTTP error
            # response.status_code = status.HTTP_404_NOT_FOUND    #can also be hardcode to 404
            # return {"msg": f"post with id {id} was not found"}
            # a better way to do this will be the following, raising HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    """
    post_index = find_post_index(id)
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    else:
        my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    """
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    deleted_post = cursor.fetchone()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    
    conn.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

    

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id),)) 
    #post_index = find_post_index(id)
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")

    #post_dict = post.dict()
    #post_dict["id"] = id
    #my_posts[post_index] = post_dict
    return{"data": updated_post}
