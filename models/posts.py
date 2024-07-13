from pydantic import BaseModel
from typing import Optional
class Post(BaseModel):
    id: str
    content: str
    thread_id: str
    owner_id: str
    created_at: str
    updated_at: str

class NewPost(BaseModel):
    content: str
    thread_id: str

class UpdatePost(BaseModel):
    content: str
    thread_id: str