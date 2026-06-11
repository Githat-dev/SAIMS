from pydantic import BaseModel

class SaleItemCreate(BaseModel):
    product_id: int
    quantity: int

class SaleCreate(BaseModel):
    user_id: int
    items: list[SaleItemCreate]

class SaleResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float

    class Config:
        from_attributes = True