from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.deps import get_current_user
from app.core.rbac import require_role
from app.services.role_servcie import get_roles, create_role

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def list_roles(db: Session = Depends(get_db), user=Depends(require_role(1))):
    return get_roles(db)

@router.post("/")
def add_role(name: str, db: Session = Depends(get_db), user=Depends(require_role(1))):
    return create_role(db, name)