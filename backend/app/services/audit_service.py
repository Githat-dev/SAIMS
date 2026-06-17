from app.models.audit_log import AuditLog

def create_audit_log(
        db,
        user_id: int,
        action: str
):

    log = AuditLog(
        user_id=user_id,
        action=action
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log