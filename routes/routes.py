from fastapi import APIRouter
from handlers.hello import hello_world

router = APIRouter()

@router.get('/')
def root():
    return hello_world()