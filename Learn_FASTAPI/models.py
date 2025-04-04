
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, primary_key = False, nullable = False)
    content = Column(String, primary_key = False, nullable = False)
    published = Column(Boolean, nullable = False, server_default = 'True')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))

class User(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key = True, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))

