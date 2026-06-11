from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.deps import get_current_user
from app.core.rbac import require_role
from app.services.user_service import (
    get_all_users, 
    get_user_by_id
    )

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)