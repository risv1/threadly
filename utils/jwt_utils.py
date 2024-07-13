from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import getenv

load_dotenv()
jwt_secret = getenv('JWT_SECRET')

def create_jwt_token(user_id: int) -> str:
    claims = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(claims, jwt_secret, algorithm='HS256')
    return token

def decode_jwt_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, jwt_secret, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')