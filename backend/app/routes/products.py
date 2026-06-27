from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.product import ProductCreate
from app.core.rbac import require_role
from app.services.product_service import (
    create_product,
    get_products,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1,2))
):
    return create_product(db, product)

@router.get("/")
def list_products(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1,2,3,4))
):
    return get_products(db)

@router.put("/product_id")
def edit_product(
    product_id: int,
    product: ProductCreate,
    db: Session =Depends(get_db),
    current_user = Depends(require_role(1,2))
):
    return update_product(
        db,
        product_id,
        product
    )

@router.delete("/product_id")
def remove_product(
    product_id: int,
    db: Session =Depends(get_db),
    current_user = Depends(require_role(1))
):
    return delete_product(
        db,
        product_id,    )