from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get("sub")
        role_id: int = payload.get("role_id")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"username": username, "role_id": role_id}
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid or expired")