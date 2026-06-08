from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    sku = Column(String(50), unique=True, nullable=False)

    price = Column(Float, nullable=False)

    quantity = Column(Integer, default=0)

    low_stock_threshold = Column(Integer, default=10)

    category_id = Column(Integer, ForeignKey("categories.id"))

    created_at = Column(DateTime, default=func.now())
    
    category = relationship("Category")