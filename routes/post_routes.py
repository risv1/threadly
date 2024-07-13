from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from models.posts import UpdatePost, NewPost
from database.db import get_session
from handlers.post_handlers import create_post, update_post, delete_post, get_thread_posts

router = APIRouter()

@router.post("/create")
def create(post: NewPost, db: Session = Depends(get_session), req: Request = Request):
    return create_post(post, db, req)

@router.get("/thread/{thread_id}")
def get_thread_posts(thread_id: str, db: Session = Depends(get_session)):
    return get_thread_posts(thread_id, db)

@router.put("/update/{post_id}")
def update(post_id: str, post: UpdatePost, db: Session = Depends(get_session), req: Request = Request):
    return update_post(post_id, post, db, req)

@router.delete("/delete/{post_id}")
def delete(post_id: str, db: Session = Depends(get_session)):
    return delete_post(post_id, db)

