from app.models.users import User
from app.services.audit_service import create_audit_log
from app.core.security import hash_password
from app.services.notification_service import create_notification

def get_all_users(db):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role_id": user.role_id,
            "is_active": user.is_active
        }
        for user in users
    ]

def get_user_by_id(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role_id": user.role_id,
        "is_active": user.is_active
    }

def create_user(db, user_data):

    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        role_id=user_data.role_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    create_notification(
        db=db,
        #TODO : Replace with dynamic Superadmin lookup
        user_id=1,
        title="New User Created",
        message=f"User '{user.username}' was created successfully."
    )

    create_audit_log(
        db,
        user.id,
        f"Created user: {user.username}"
    )

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role_id": user.role_id,
        "is_active": user.is_active
    }

def get_users(db):
    return db.query(User).all()


def update_user(db, user_id, user_data):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None
    
    if user_data.username is not None:
        user.username = user_data.username

    if user_data.email is not None:
        user.email = user_data.email

    if user_data.role_id is not None:
        user.role_id = user_data.role_id

    if user_data.is_active is not None:
        user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)

    return user

def delete_user(db, user_id: int):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None
    
    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}