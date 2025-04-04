from fastapi import Depends, FastAPI, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from database import get_db
import models, schemas, utils

router = APIRouter(
    tags=['Users']
)

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)    
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} does not exist")
    return user