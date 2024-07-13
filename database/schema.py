from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

class Threads(Base):
    __tablename__ = 'threads'
    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(String, primary_key=True)
    content = Column(String)
    owner_id = Column(String)
    thread_id = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(String, primary_key=True)
    content = Column(String)
    post_id = Column(String)
    owner_id = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
