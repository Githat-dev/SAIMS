from fastapi import Depends, HTTPException
from app.core.deps import get_current_user

def require_role(*allowed_roles):

    def role_checker(user=Depends(get_current_user)):
        role_id = user.get("role_id")

        if role_id not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )
        
        return user
    
    return role_checker