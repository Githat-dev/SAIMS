from fastapi import HTTPException
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product
from app.services.notification_service import create_notification

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
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        
        if product.quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )
        
        subtotal = product.price * item.quantity

        total_amount += subtotal
        
        product.quantity -= item.quantity

        if product.quantity == 0:
            
            create_notification(
                db=db,
                user_id=1,
                title="Out of stock",
                message=f"{product.name} is now out of stock."
            )
            create_notification(
                db=db,
                user_id=2,
                title="Out of stock",
                message=f"{product.name} is now out of stock."
            )

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

    HIGH_VALUE_SALE = 3000

    if sale.total_amount >= HIGH_VALUE_SALE:
        
        create_notification(
            db=db,
            user_id=1,
            title="High Value Sale",
            message=f"A high-value sale of \u20A6{sale.total_amount:,.2f} has been recorded."
        )

        create_notification(
            db=db,
            user_id=2,
            title="High Value Sale",
            message=f"A high-value sale of \u20A6{sale.total_amount:,.2f} has been recorded."
        )

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