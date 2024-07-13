from pydantic import BaseModel
from typing import Optional

class NewThread(BaseModel):
    title: str
    content: str

class UpdateThread(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None