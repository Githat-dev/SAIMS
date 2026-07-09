from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.config import SECRET_KEY, ALGORITHM
from app.core.database import SessionLocal
from app.models.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get("sub")
        role_id: int = payload.get("role_id")
        user_id: int = payload.get("user_id")

        db = SessionLocal()

        user = db.query(User).filter(User.username == username).first()

        db.close()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return {
            "user_id": user_id,
            "username": username,
            "role_id": role_id
        }
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token invalid or expired"
        )