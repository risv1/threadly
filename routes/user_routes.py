from fastapi import APIRouter
from handlers.user_handlers import get_profile, update_profile, delete_profile

router = APIRouter()

@router.get("/profile")
def get_profile():
    return get_profile()

@router.put("/update")
def update_profile():
    return update_profile()

@router.delete("/delete")
def delete_profile():
    return delete_profile()