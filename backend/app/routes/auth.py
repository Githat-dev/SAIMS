from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.auth_service import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(username: str, email: str, password: str, role_id: int, db: Session = Depends(get_db)):
    return register_user(db, username, email, password, role_id)

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return authenticate_user(db, username, password)