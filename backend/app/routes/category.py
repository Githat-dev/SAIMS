from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.rbac import require_role
from app.services.category_service import (
    get_all_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category
)

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate
)

router = APIRouter (
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/")
def list_categories(
    db: Session = Depends(get_db),
    current_user =Depends(require_role(1,2,3,4))
):
    return get_all_categories(db)

@router.get("/{category_id}")
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user =Depends(require_role(1,2,3,4))
):
    return get_category_by_id(db, category_id)

@router.post("/")
def create_new_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user =Depends(require_role(1,2))
):
    return create_category(db, category)

@router.put("/{category_id}")
def update_existing_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user =Depends(require_role(1,2))
):
    return update_category(db, category_id, category)

@router.delete("/{category_id}")
def remove_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user =Depends(require_role(1))
):
    return delete_category(db, category_id)