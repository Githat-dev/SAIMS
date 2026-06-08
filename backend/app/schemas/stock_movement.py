from pydantic import BaseModel

class StockMovementCreate(BaseModel):
    product_id: int
    movement_type: str
    quantity: int
    reason: str

class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    movement_type: str
    quantity: int
    reason: str

    class Config:
        from_attributes = True