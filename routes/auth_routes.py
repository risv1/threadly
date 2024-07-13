from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session
from models.users import RegisterUser, LoginUser
from database.db import get_session
from handlers.auth_handlers import register_user, login_user, logout_user

router = APIRouter()

@router.post("/register")
def register(user: RegisterUser, db: Session = Depends(get_session)):
    return register_user(user, db)

@router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_session), res: Response = Response()):
    return login_user(user, db, res)

@router.post("/logout")
def logout(req: Request, res: Response):
    return logout_user(req, res)
    