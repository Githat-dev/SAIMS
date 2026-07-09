from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base

class Settings(Base):
    __tablename__ = "business_settings"

    id = Column(Integer, primary_key=True, index=True)

    business_name = Column(String, nullable=False)
    business_address = Column(String, nullable=False)
    business_phone = Column(String, nullable=True)
    business_email = Column(String, nullable=True)

    currency_symbol = Column(String, default="NGN")

    tax_percentage = Column(Float, default=0.0)

    receipt_footer = Column(
        String,
        default="Thank you for your patronage."
    )

    low_stock_threshold = Column(Integer, default=10)

    timezone = Column(
        String,
        default="Africa/Lagos"
    )

    business_logo = Column(String, nullable=True)