from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product

def create_sale(db, sale_data):
    total_amount = 0

    sale = Sale(
        user_id=sale_data.user_id,
        total_amount=0
    )

    db.add(sale)
    db.flush()

    for item in sale_data.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:
            return {"error": "Product not found"}
        
        if product.quantity < item.quantity:
            return {"error": "Insufficient stock"}
        
        subtotal = product.price * item.quantity

        total_amount += subtotal
        
        product.quantity -= item.quantity

        sale_item = SaleItem(
            sale_id=sale.id,
            product_id=product.id,
            quantity=item.quantity,
            unit_price=product.price,
            subtotal=subtotal
        )

        db.add(sale_item)

    sale.total_amount = total_amount

    db.commit()

    db.refresh(sale)

    return sale

def get_sales(db):
    return db.query(Sale).all()


def get_sale_by_id(db, sale_id):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        return {"error": "Sale not found"}
    
    sale_items = db.query(SaleItem).filter(
        SaleItem.sale_id == sale.id
    )

    items = []

    for item in sale_items:

        items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
            "subtotal": item.subtotal
        })

        return {
            "sale_id": sale.id,
            "user_id": sale.user_id,
            "total_amount": sale.total_amount,
            "created_at": sale.created_at,
            "items": items
        }