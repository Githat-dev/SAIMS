from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.rbac import require_role
from app.models.product import Product

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.post("/")
def get_low_stock_prdouct(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1,2))    
):
    products = db.query(Product).all()
    low_stock_products = []

    for product in products:

        if product.quantity <= product.low_stock_threshold:

            low_stock_products.append({
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "threshold": product.low_stock_threshold
            })

    return low_stock_products

@router.get("/summary")
def inventory_summary(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1,2))    
):

    products = db.query(Product).all()
    total_products = len(products)

    total_stock_units = sum(
        product.quantity for product in products
    )

    low_stock_products = len([
        product for product in products
        if product.quantity <= product.low_stock_threshold
    ])

    return {
        "total_products": total_products,
        "total_stock_units": total_stock_units,
        "low_stock_products": low_stock_products
    }

@router.get("/search")
def search_products(
    q: str = Query(...),
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1,2,3,4))
):
    products = db.query(Product).all()
    results = []

    for product in products:
        if q.lower() in product.name.lower():

            results.append({
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "price": product.price
            })

    return results

@router.get("/report")
def inventory_report(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1,2))    
):

    products = db.query(Product).all()

    report = []

    for product in products:

        report.append({

            "id": product.id,
            "name": product.name,
            "sku": product.sku,
            "quantity": product.quantity,
            "threshold": product.low_stock_threshold,
            "status": ("LOW STOCK" if product.quantity <= product.low_stock_threshold else "IN STOCK")
        })

    return report