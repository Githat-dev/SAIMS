from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.rbac import require_role
from app.services.audit_service import get_all_audit_logs

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)

@router.get("/")
def list_audit_logs(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(1))
):
    return get_all_audit_logs(db)