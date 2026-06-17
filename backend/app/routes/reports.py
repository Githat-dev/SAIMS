from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.report_service import (
    get_sales_report,
    get_inventory_report,
    get_stock_movement_report,
    get_user_report
    )
from app.services.report_service import get_audit_report

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/sales")
def sales_report(
    db: Session = Depends(get_db)
):
    return get_sales_report(db)

@router.get("/inventory")
def inventory_report(
    db: Session = Depends(get_db)
):
    return get_inventory_report(db)

@router.get("/stock-movements")
def stock_movement_report(
    db: Session = Depends(get_db)
):
    return get_stock_movement_report(db)

@router.get("/users")
def user_report(
    db: Session = Depends(get_db)
):
    return get_user_report(db)

@router.get("/audit")
def audit_report(
    db: Session = Depends(get_db)
):
    return get_audit_report(db)