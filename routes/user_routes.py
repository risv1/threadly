from fastapi import APIRouter, Depends, Request
from database.db import get_session
from sqlalchemy.orm import Session
from models.users import UpdateUser
from handlers.user_handlers import get_profile, update_profile, delete_profile

router = APIRouter()

@router.get("/profile")
def get_profile(db: Session = Depends(get_session), req: Request = Request):
    return get_profile(db, req)

@router.put("/update")
def update_profile(user: UpdateUser, db: Session = Depends(get_session), req: Request = Request):
    return update_profile(user, db, req)

@router.delete("/delete")
def delete_profile(db: Session = Depends(get_session), req: Request = Request):
    return delete_profile(db, req)