from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.settings import Settings

def get_settings(db: Session):

    settings = db.query(Settings).first()

    if not settings:

        settings = Settings(
            business_name="Tea & Spice",
            business_address="Nasarawa state, Nigeria.",
            business_phone="+2347043435533",
            business_email="info@teaandspice.com",
            currency_symbol="NGN",
            tax_percentage="0.0",
            receipt_footer="Thank you for your patronage.",
            low_stock_threshold=10,
            timezone="Africa/Lagos"
        )

        db.add(settings)
        try:
            db.commit()
            db.refresh(settings)
        except Exception as e:
            db.rollback()
            print(e)
            raise

    return settings
    
def update_settings(db: Session, data: dict):

    settings = get_settings(db)

    print("SETTINGS =", settings)
    print("TYPE=", type(settings))

    if settings is None:
        raise Exception("get_settings() returned None")

    for key, value in data.items():
        setattr(settings, key, value)

    db.commit()
    db.refresh(settings)

    return settings