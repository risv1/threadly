from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from models.comments import NewComment, UpdateComment
from database.db import get_session
from handlers.comment_handlers import create_comment, get_post_comments, update_comment, delete_comment

router = APIRouter()

@router.post("/create")
def create(comment: NewComment, db: Session = Depends(get_session), req: Request = Request):
    return create_comment(comment, db, req)

@router.get("/post/{post_id}")
def get_comments(post_id: str, db: Session = Depends(get_session)):
    return get_post_comments(post_id, db)

@router.put("/update/{comment_id}")
def update(comment: UpdateComment, db: Session = Depends(get_session), req: Request = Request):
    return update_comment(comment, db, req)

@router.delete("/delete/{comment_id}")
def delete(comment_id: str, db: Session = Depends(get_session)):
    return delete_comment(comment_id, db)
