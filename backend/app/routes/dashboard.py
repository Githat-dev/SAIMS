from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.deps import get_current_user
from app.services.dashboard_service import (
    get_dashboard_summary,
    get_top_selling_products,
    get_sales_trend,
    get_inventory_value,
    get_low_stock_products,
    get_monthly_revenue
)

 
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_dashboard_summary(db)

@router.get("/top-products")
def top_products(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_top_selling_products(db)

@router.get("/sales-trend")
def sales_trend(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_sales_trend(db)

@router.get("/inventory-value")
def inventory_value(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_inventory_value(db)

@router.get("/low-stock")
def low_stock(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_low_stock_products(db)

@router.get("/monthly-revenue")
def monthly_revenue(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_monthly_revenue(db)