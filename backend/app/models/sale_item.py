from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base

class SaleItem(Base):
    __tablename__ = "sales_items"

    id = Column(Integer, primary_key=True, index=True)

    sale_id = Column(Integer, ForeignKey("sales.id"))

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False)

    unit_price = Column(Float, nullable=False)

    subtotal = Column(Float, nullable=False)