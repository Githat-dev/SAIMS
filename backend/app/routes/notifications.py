from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.deps import get_current_user
from app.services.notification_service import (
    get_notifications,
    mark_notification_read,
    delete_notification
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.get("/")
def list_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_notifications(
        db,
        current_user["user_id"]
    )

@router.post("/notification_id")
def read_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return mark_notification_read(
        db,
        notification_id,
        current_user["user_id"]
    )

@router.delete("/{notification_id}")
def remove_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return delete_notification(
        db,
        notification_id,
        current_user["user_id"]
    )