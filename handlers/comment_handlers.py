from fastapi import HTTPException
from models.comments import Comment

def create_comment(comment: Comment):
    return comment

def get_post_comments():
    return []

def update_comment(comment: Comment):
    return comment

def delete_comment(comment_id: str):
    return comment_id