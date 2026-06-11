from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.sale import (
    SaleCreate
    )
from app.services.sales_service import (
    create_sale,
    get_sales,
    get_sale_by_id
)

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

@router.post("/")
def create_sale_route(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):
    return create_sale(
        db,
        sale
    )

@router.get("/")
def list_sales(
    db: Session = Depends(get_db)
):
    return get_sales(db)

@router.get("/summary")
def sales_summary(db: Session = Depends(get_db)):

    sales = get_sales(db)

    total_sales = len(sales)

    total_revenue = sum(
        sale.total_amount
        for sale in sales
    )

    average_sales_value =(
        total_revenue / total_sales
        if total_sales > 0
        else 0
    )

    return {
        "total_sales": total_sales,
        "total_revenue": total_revenue,
        "average_sales_value": average_sales_value
    }

@router.get("/{sale_id}")
def get_sale(
        sale_id: int,
        db: Session = Depends(get_db)
    ):

    return get_sale_by_id(db, sale_id)