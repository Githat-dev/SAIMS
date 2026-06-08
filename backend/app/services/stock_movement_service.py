from app.models.stock_movement import StockMovement
from app.models.product import Product

def create_stock_movement(db, movement_data):

    product = db.query(Product).filter(
        Product.id == movement_data.product_id
    ).first()

    if not product:
        return {"error": "Product not found"}
    
    if movement_data.movement_type.lower() == "in":
        product.quantity += movement_data.quantity

    elif movement_data.movement_type.lower() == "out":

        if product.quantity < movement_data.quantity:
            return {"error": "Insufficient stock"}
        
        product.quantity -= movement_data.quantity

    movement = StockMovement(
        product_id=movement_data.product_id,
        movement_type=movement_data.movement_type,
        quantity=movement_data.quantity,
        reason=movement_data.reason
    )

    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement

def get_stock_movements(db):
    return db.query(
        StockMovement
    ).all()