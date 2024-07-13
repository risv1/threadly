from fastapi import HTTPException
from models.posts import Post

def create_post(post: Post):
    return post

def get_thread_posts():
    return []

def update_post(post: Post):
    return post

def delete_post(post_id: str):
    return post_id

