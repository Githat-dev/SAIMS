from app.models.product import Product
from app.models.sale import Sale
from app.models.users import User

def get_dashboard_summary(db):

    total_products = db.query(Product).count()

    low_stock_products = db.query(Product).filter(
        Product.quantity <= Product.low_stock_threshold
    ).count()

    total_sales = db.query(Sale).count()

    total_users = db.query(User).count()

    return {
        "total_products": total_products,
        "low_stock_products": low_stock_products,
        "total_sales": total_sales,
        "total_users": total_users
    }