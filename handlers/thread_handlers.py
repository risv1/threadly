from fastapi import HTTPException
from models.threads import Thread

def create_thread(thread: Thread):
    return thread

def get_all_threads():
    return []

def get_thread_by_id(thread_id: str):
    return thread_id

def update_thread(thread: Thread):
    return thread

def delete_thread(thread_id: str):
    return thread_id