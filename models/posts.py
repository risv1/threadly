from pydantic import BaseModel
from typing import Optional

class NewPost(BaseModel):
    content: str
    thread_id: str

class UpdatePost(BaseModel):
    content: Optional[str] = None
    thread_id: Optional[str] = None