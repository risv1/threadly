from fastapi import APIRouter
from models.threads import Thread
from handlers.thread_handlers import create_thread, get_all_threads, get_thread_by_id, update_thread, delete_thread

router = APIRouter()

@router.post("/create")
def create(thread: Thread):
    return create_thread(thread)

@router.get("/all")
def get_all():
    return get_all_threads()

@router.get("/{thread_id}")
def get_by_id(thread_id: str):
    return get_thread_by_id(thread_id)

@router.put("/update/{thread_id}")
def update(thread: Thread):
    return update_thread(thread)

@router.delete("/delete/{thread_id}")
def delete(thread_id: str):
    return delete_thread(thread_id)
