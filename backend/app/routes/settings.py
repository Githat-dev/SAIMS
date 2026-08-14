from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from pathlib import Path
import shutil
import os
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.deps import get_current_user
from app.services.settings_service import get_settings, update_settings

router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)

@router.get("/")
def read_settings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_settings(db)

@router.put("/")
def edit_settings(
    data: dict,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_settings(db, data)

@router.post("/logo")
def uplaod_logo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    
    settings = get_settings(db)

    if settings.business_logo:
        old_logo = Path(settings.business_logo)

        if old_logo.exists():
            os.remove(old_logo)

    extension = os.path.splitext(file.filename)[1]

    filename = f"business_logo{extension}"

    filepath = Path("uploads/logos") / filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    settings.business_logo = str(filepath)

    db.commit()
    db.refresh(settings)

    return {
        "message": "Business logo uploaded successfully.",
        "logo_path": settings.business_logo
    }