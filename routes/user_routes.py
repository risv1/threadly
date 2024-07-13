from fastapi import APIRouter
from models.users import User
from handlers.user_handlers import get_profile, update_profile, delete_profile

router = APIRouter()

@router.get("/profile")
def get_profile(user: User):
    return get_profile(user)

@router.put("/update")
def update_profile(user: User):
    return update_profile(user)

@router.delete("/delete")
def delete_profile(user: User):
    return delete_profile(user)