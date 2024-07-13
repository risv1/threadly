from pydantic import BaseModel

class Post(BaseModel):
    id: str
    content: str
    thread_id: str
    owner_id: str
    created_at: str
    updated_at: str