from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from database.schema import Posts
from models.posts import NewPost, UpdatePost
from utils.jwt_utils import decode_jwt_token

def create_post(post: NewPost, db: Session, req: Request):
    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)

    new_post = Posts (
        id=str(uuid4()),
        content=post.content,
        owner_id=str(token_data["user_id"]),
        thread_id=post.thread_id,
        created_at=str(datetime.utcnow()),
        updated_at=str(datetime.utcnow())
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return { "message": "Post created successfully", "post": new_post }

def get_thread_posts(thread_id: str, db: Session):
    find_thread = db.query(Posts).filter(Posts.thread_id == thread_id).all()
    if not find_thread:
        raise HTTPException(status_code=404, detail="No posts found")
    
    find_posts = db.query(Posts).filter(Posts.thread_id == thread_id).all()
    if not find_posts:
        raise HTTPException(status_code=404, detail="No posts found")
    
    if find_posts == []: 
        raise HTTPException(status_code=404, detail="No posts found")
    
    return { "message": "Posts found", "posts": find_posts }

def update_post(post_id: str, post: UpdatePost, db: Session, req: Request):
    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)
    user_id = str(token_data["user_id"])

    find_post = db.query(Posts).filter(Posts.id == post_id).first()
    if not find_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if find_post.owner_id != user_id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this post")

    if post.content:
        find_post.content = post.content
    if post.thread_id:
        find_post.thread_id = post.thread_id
    find_post.updated_at = str(datetime.utcnow())

    db.commit()
    db.refresh(find_post)

    return { "message": "Post updated successfully", "post": find_post }

def delete_post(post_id: str, db: Session):
    find_post = db.query(Posts).filter(Posts.id == post_id).first()
    if not find_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(find_post)
    db.commit()

    return { "message": "Post deleted successfully" }
    

