from app.core.security import hash_password, verify_password
from app.models.users import User
from app.core.jwt import create_access_token

def register_user(db, username, email, password, role_id):
    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role_id=role_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(db, username, password):
    user = db.query(User).filter(User.username == username). first()

    if not user:
        return None
    
    if not verify_password(password, user.password_hash):
        return None

    print("USER:", user.username)
    print("ROLE:", user.role_id)
    
    token = create_access_token(
        data={"sub": user.username, "role_id": user.role_id}
    )

    print ("TOKEN:", token)

    return {
        "access_token": token,
        "token_type": "bearer"
    }