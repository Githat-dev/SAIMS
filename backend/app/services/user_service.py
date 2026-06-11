from app.models.users import User

def get_all_users(db):
    return db.query(User).all()

def get_user_by_id(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db):
    return db.query(User).all()