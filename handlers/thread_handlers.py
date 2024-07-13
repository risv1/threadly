from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.threads import NewThread, UpdateThread
from database.schema import Threads
from utils.jwt_utils import decode_jwt_token

def create_thread(thread: NewThread, db: Session, req: Request):

    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)

    new_thread = Threads (
        id=str(uuid4()),
        title=thread.title,
        content=thread.content,
        owner_id=str(token_data["user_id"]),
        created_at=str(datetime.utcnow()),
        updated_at=str(datetime.utcnow())
    )
    db.add(new_thread)
    db.commit()
    db.refresh(new_thread)

    return { "message": "Thread created successfully", "thread": new_thread }

def get_all_threads(db: Session):
    all_threads = db.query(Threads).all()
    if not all_threads:
        raise HTTPException(status_code=404, detail="No threads found")
    
    if all_threads == []:
        return JSONResponse(content={"message": "No threads found"}, status_code=404)

    return { "threads": all_threads }

def get_thread_by_id(thread_id: str, db: Session):
    thread = db.query(Threads).filter(Threads.id == thread_id).first()
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    
    return { "thread": thread, "message": "Thread found" }

def update_thread(thread_id: str, thread: UpdateThread, db: Session):
    find_thread = db.query(Threads).filter(Threads.id == thread_id).first()
    if not find_thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    
    if thread.title:
        find_thread.title = thread.title
    if thread.content:
        find_thread.content = thread.content
    find_thread.updated_at = str(datetime.utcnow())

    db.commit()
    db.refresh(find_thread)

    return { "message": "Thread updated successfully", "thread": find_thread }

def delete_thread(thread_id: str, db: Session):
    find_thread = db.query(Threads).filter(Threads.id == thread_id).first()
    if not find_thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    
    db.delete(find_thread)
    db.commit()

    return { "message": "Thread deleted successfully" }