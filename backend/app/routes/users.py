from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.deps import get_current_user
from app.core.rbac import require_role
from app.services.user_service import (
    get_all_users, 
    get_user_by_id,
    create_user,
    update_user,
    delete_user
    )
from app.schemas.user import (
    UserCreate,
    UserUpdate
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@router.post("/{user_id}")
def create_new_user(
        user: UserCreate,
        db: Session =Depends(get_db)
):
    return create_user(db, user)

@router.put("/{user_id}")
def update_existing_user(
    user_id: int,
    user: UserUpdate,
    db: Session =Depends(get_db)
):
    return update_user(db, user_id, user)

@router.delete("/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(db, user_id)