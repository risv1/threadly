from pydantic import BaseModel

class NewComment(BaseModel):
    content: str
    post_id: str

class UpdateComment(BaseModel):
    content: str