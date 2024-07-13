from fastapi import APIRouter
from models.comments import Comment
from handlers.comment_handlers import create_comment, get_post_comments, update_comment, delete_comment

router = APIRouter()

@router.post("/create")
def create(comment: Comment):
    return create_comment(comment)

@router.get("/post/{post_id}")
def get_comments(post_id: str):
    return get_post_comments(post_id)

@router.put("/update/{comment_id}")
def update(comment: Comment):
    return update_comment(comment)

@router.delete("/delete/{comment_id}")
def delete(comment_id: str):
    return delete_comment(comment_id)
