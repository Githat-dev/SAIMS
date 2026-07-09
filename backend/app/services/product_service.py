from app.models.product import Product
from app.services.notification_service import create_notification

def create_product(db, product_data):

    product = Product(
        name=product_data.name,
        sku=product_data.sku,
        price=product_data.price,
        quantity=product_data.quantity,
        low_stock_threshold=product_data.low_stock_threshold,
        category_id=product_data.category_id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

def get_products(db):
    return db.query(Product).all()

def update_product(db, product_id, product_data):
    
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None
    
    product.name = product_data.name
    product.sku = product_data.sku
    product.price = product_data.price
    product.quantity = product_data.quantity
    product.low_stock_threshold = product_data.low_stock_threshold
    product.category_id = product_data.category_id

    db.commit()
    db.refresh(product)

    if product.quantity <= product.low_stock_threshold:

        create_notification(
            db=db,
            user_id=1,
            title="Low Stock Alerts",
            message=f"'{product.name}' is running low ({product.quantity} remaining)."
        )

        create_notification(
            db=db,
            user_id=2,
            title="Low Stock Alerts",
            message=f"'{product.name}' is running low ({product.quantity} remaining)."
        )

    return product

def delete_product(db , product_id):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None
    
    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}