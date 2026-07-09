from sqlalchemy import func
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product
from app.models.users import User

def get_dashboard_summary(db):

    total_products = db.query(Product).count()

    low_stock_products = db.query(Product).filter(
        Product.quantity <= Product.low_stock_threshold
    ).count()

    total_sales = db.query(Sale).count()

    total_users = db.query(User).count()

    total_revenue = (
        db.query(func.sum(Sale.total_amount)).scalar() or 0
    )

    products_sold = (
        db.query(func.sum(SaleItem.quantity)).scalar() or 0
    )

    inventory_value = (
        db.query(func.sum(Product.price * Product.quantity)).scalar() or 0
    )

    out_of_stock_products = (
        db.query(Product).filter(Product.quantity == 0).count()
    )

    return {
        "total_products": total_products,
        "low_stock_products": low_stock_products,
        "total_sales": total_sales,
        "total_users": total_users,
        "total_revenue": total_revenue,
        "product_sold": products_sold,
        "inventory_value": inventory_value,
        "out_of_stock_products": out_of_stock_products
    }

def get_top_selling_products(db):

    results = (
        db.query(
            Product.name, 
            func.sum(SaleItem.quantity).label("quantity_sold")).join(SaleItem, Product.id == SaleItem.product_id).group_by(Product.id).order_by(func.sum(SaleItem.quantity).desc()).all()
    )
    return [
        {
            "product": product,
            "quantity_sold": quantity
        }
        for product, quantity in results
    ]

def get_sales_trend(db):
    results = (
        db.query(
            func.date(Sale.created_at).label("date"), func.sum(Sale.total_amount).label("revenue")
        ).group_by(func.date(Sale.created_at)).order_by(func.date(Sale.created_at)).all()
    )

    return [
        {
            "date": date,
            "revenue": revenue
        }
        for date, revenue in results
    ]

def get_inventory_value(db):
    inventory_value = (
        db.query(
            func.sum(Product.price * Product.quantity)
        ).scalar()
    )

    return {
        "inventory_value": inventory_value or 0
    }

def get_low_stock_products(db):
    results = (
        db.query(Product.name, Product.quantity).filter(Product.quantity <= 10).all()
    )

    return [
        {
            "product": product,
            "stock": stock
        }
        for product, stock in results
    ]

def get_monthly_revenue(db):
    results = (
        db.query(
            func.strftime("%Y-%m", Sale.created_at).label("month"),
            func.sum(Sale.total_amount).label("revenue")
        ).group_by(func.strftime("%Y-%m", Sale.created_at)).order_by(func.strftime("%Y-%m", Sale.created_at)).all()
    )

    return [
        {
            "month": month,
            "revenue": revenue
        }
        for month, revenue in results
    ]