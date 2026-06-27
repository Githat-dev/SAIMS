from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.product import Product

def get_inventory_summary(db: Session):
    total_products = db.query(Product).count()

    total_stock = (
        db.query(func.sum(Product.quantity)).scalar()
    ) or 0

    total_value = (
        db.query(func.sum(Product.quantity * Product.price)).scalar()
    ) or 0

    return {
        "total_products": total_products,
        "total_stock": total_stock,
        "total_inventory_value": total_value
    }

def search_inventory(db: Session, keyword: str):
    return (
        db.query(Product).flter(Product.name.ilike(f"%{keyword}%")).all()
    )

def generate_inventory_report(db: Session):
    return (
        db.query(Product).order_by(Product.name.asc()).all()
    )

def check_low_stock(db: Session):
    return (
        db.query(Product).filter(Product.quantity <= Product.low_stock_threshold).all()
    )