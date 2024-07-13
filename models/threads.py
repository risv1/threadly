from pydantic import BaseModel

class Thread(BaseModel):
    id: str
    title: str
    content: str
    owner_id: str
    created_at: str
    updated_at: str