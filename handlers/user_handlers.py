from fastapi import HTTPException
from models.users import User

def get_profile(user: User):
    return user

def update_profile(user: User):
    return user

def delete_profile(user: User):
    return user