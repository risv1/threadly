from fastapi import APIRouter
from models.posts import Post
from handlers.post_handlers import create_post, update_post, delete_post, get_thread_posts

router = APIRouter()

@router.post("/create")
def create(post: Post):
    return create_post(post)

@router.get("/thread/{thread_id}")
def get_thread(thread_id: str):
    return get_thread_posts(thread_id)

@router.put("/update/{post_id}")
def update(post: Post):
    return update_post(post)

@router.delete("/delete/{post_id}")
def delete(post_id: str):
    return delete_post(post_id)

