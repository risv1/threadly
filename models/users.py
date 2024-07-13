from pydantic import BaseModel
from typing import Optional

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None