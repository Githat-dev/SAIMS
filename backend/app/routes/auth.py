from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.dependencies import get_db
from app.services.auth_service import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(username: str, email: str, password: str, role_id: int, db: Session = Depends(get_db)):
    return register_user(db, username, email, password, role_id)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return user