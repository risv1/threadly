from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from models.threads import NewThread, UpdateThread
from database.db import get_session
from handlers.thread_handlers import create_thread, get_all_threads, get_thread_by_id, update_thread, delete_thread

router = APIRouter()

@router.post("/create")
def create(thread: NewThread, db: Session = Depends(get_session), req: Request = Request):
    return create_thread(thread, db, req)

@router.get("/all")
def get_all(db: Session = Depends(get_session)):
    return get_all_threads(db)

@router.get("/{thread_id}")
def get_by_id(thread_id: str, db: Session = Depends(get_session)):
    return get_thread_by_id(thread_id, db)

@router.put("/update/{thread_id}")
def update(thread_id: str, thread: UpdateThread, db: Session = Depends(get_session)):
    return update_thread(thread_id, thread, db)

@router.delete("/delete/{thread_id}")
def delete(thread_id: str, db: Session = Depends(get_session)):
    return delete_thread(thread_id, db)
