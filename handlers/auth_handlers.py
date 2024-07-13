from datetime import datetime
from uuid import uuid4
from datetime import timedelta
from fastapi import HTTPException, Response, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.users import RegisterUser, LoginUser
from database.schema import User
from utils.hash_utils import hash_password, verify_password
from utils.jwt_utils import create_jwt_token

def register_user(user: RegisterUser, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)

    new_user = User (
        id=str(uuid4()),
        name=user.name,
        email=user.email,
        password=hashed_password,
        created_at=str(datetime.utcnow()),
        updated_at=str(datetime.utcnow())
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse(status_code=201, content={"message": "User registered successfully"})

def login_user(user: LoginUser, db: Session, res: Response):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
    
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
    token = create_jwt_token(existing_user.id)

    res = JSONResponse(status_code=200, content={"message": "User logged in successfully"})
    res.set_cookie(key="token", value=token, httponly=True, expires=timedelta(days=1))

    return res
    
def logout_user(req: Request, res: Response):
    check_cookie = req.cookies.get("token")
    if not check_cookie:
        raise HTTPException(status_code=400, detail="User not logged in")
    
    res = JSONResponse(status_code=200, content={"message": "User logged out successfully"})
    res.delete_cookie(key="token")

    return res
