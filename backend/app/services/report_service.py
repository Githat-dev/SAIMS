from app.models.sale import Sale
from app.models.product import Product
from app.models.stock_movement import StockMovement
from app.models.users import User

def get_sales_report(db):

    sales = db.query(Sale).all()

    total_revenue = sum(
        sale.total_price for sale in sales
    )

    return {
        "total_sales": len(sales),
        "total_revenue": total_revenue,
        "sales": sales
    }

def get_inventory_report(db):

    products = db.query(Product).all()

    return {
        "total_products": len(products),
        "products": [
            {
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "price": product.price,
                "low_stock_threshild": product.low_stock_threshold
            }
            for product in products
        ]
    }

def get_stock_movement_report(db):

    movements = db.query(StockMovement).all()

    return {
        "total_movements": len(movements),
        "movements": [
            {
                "id": movement.id,
                "product_id": movement.product_id,
                "movement_type": movement.movement_type,
                "quantity": movement.quantity,
                "created_at": movement.created_at
            }
            for movement in movements
        ]
    }

def get_user_report(db):

    users = db.query(User).all()

    return {
        "total_users": len(users),
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role_id": user.role_id,
                "is_active": user.is_active
            }
            for user in users
        ]
    }