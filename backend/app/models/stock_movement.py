from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.sql import func
from app.core.database import Base

class StockMovement(Base):

    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    movement_type = Column(String(20), nullable=False)
    quantity = Column(Integer, nullable=False)
    reason = Column(String(255))
    created_at = Column(DateTime, default=func.now())