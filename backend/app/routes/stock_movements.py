from fastapi  import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.stock_movement import (
    StockMovementCreate
)
from app.services.stock_movement_service import (
    create_stock_movement,
    get_stock_movements
)

router = APIRouter(
    prefix="/stock-movements",
    tags=["Stock Movements"]
)

@router.post("/")
def add_stock_movement(
    movement: StockMovementCreate,
    db: Session =Depends(get_db)
):
    return create_stock_movement(
        db,
        movement
    )

@router.get("/")
def list_stock_movements(
    db: Session = Depends(get_db)
):
    return get_stock_movements(db)