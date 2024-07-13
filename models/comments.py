from pydantic import BaseModel

class Comment(BaseModel):
    id: str
    content: str
    post_id: str
    owner_id: str
    created_at: str
    updated_at: str