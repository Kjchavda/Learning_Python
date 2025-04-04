from fastapi import Depends, FastAPI, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from database import get_db
import models, schemas, oauth2

router = APIRouter(
    tags=['Posts']
)

@router.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()         (used to get posts directly with SQL from psycopg2)
    posts = db.query(models.Post).all() # get posts through ORM sqlalchemy
    return posts

@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)    #status code parameter to select default status code
def create_post(post: schemas.Post, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    print(user_id)
    post_dict = post.dict()
    new_post = models.Post(**post_dict)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_post_index(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i 

@router.get("/posts/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db)): #No need to pass in response now
    """
        post = find_post(id)
    if not post:
            #Below code is a sloppy way to implement HTTP error
            # response.status_code = status.HTTP_404_NOT_FOUND    #can also be hardcode to 404
            # return {"msg": f"post with id {id} was not found"}
            # a better way to do this will be the following, raising HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    """
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()


    if not post:
            #Below code is a sloppy way to implement HTTP error
            # response.status_code = status.HTTP_404_NOT_FOUND    #can also be hardcode to 404
            # return {"msg": f"post with id {id} was not found"}
            # a better way to do this will be the following, raising HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    
    return post

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    """
    post_index = find_post_index(id)
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    else:
        my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    """
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id) 
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    
    post.delete(synchronize_session= False)
    db.commit()
    # conn.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

    

@router.put("/posts/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.Post, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id),)) 
    # #post_index = find_post_index(id)
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_qeury = db.query(models.Post).filter(models.Post.id == id) 
    post = post_qeury.first()


    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    post_qeury.update(updated_post.dict(), synchronize_session = False)
    db.commit()
    #post_dict = post.dict()
    #post_dict["id"] = id
    #my_posts[post_index] = post_dict
    return post_qeury.first()
