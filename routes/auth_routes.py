from fastapi import APIRouter
from models.users import User
from handlers.auth_handlers import register_user, login_user, logout_user

router = APIRouter()

@router.post("/register")
def register(user: User):
    return register_user(user)

@router.post("/login")
def login(user: User):
    return login_user(user)

@router.post("/logout")
def logout(user: User):
    return logout_user(user)
    