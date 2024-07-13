from datetime import datetime
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from database.schema import User
from models.users import UpdateUser
from utils.jwt_utils import decode_jwt_token

def get_profile(db: Session, req: Request):
    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)
    user_id = token_data["user_id"]
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return { "user": user, "message": "User found" }

def update_profile(user: UpdateUser, db: Session, req: Request):
    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)
    user_id = token_data["user_id"]

    find_user = db.query(User).filter(User.id == user_id).first()
    if not find_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.name:
        find_user.name = user.name
    if user.email:
        find_user.email = user.email
    find_user.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(find_user)
    
    return { "message": "User updated successfully", "user": find_user }

def delete_profile(db: Session, req: Request):
    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)
    user_id = token_data["user_id"]

    find_user = db.query(User).filter(User.id == user_id).first()
    if not find_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(find_user)
    db.commit()
    
    return { "message": "User deleted successfully" }