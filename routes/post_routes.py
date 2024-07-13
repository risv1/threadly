from fastapi import APIRouter
from models.posts import Post
from handlers.post_handlers import create_post, get_all_posts, get_post, update_post, delete_post

router = APIRouter()

@router.post("/create")
def create(post: Post):
    return create_post(post)

@router.get("/all")
def get_all():
    return get_all_posts()

@router.get("/{post_id}")
def get_by_id(post_id: str):
    return get_post(post_id)

@router.put("/update/{post_id}")
def update(post: Post):
    return update_post(post)

@router.delete("/delete/{post_id}")
def delete(post_id: str):
    return delete_post(post_id)

