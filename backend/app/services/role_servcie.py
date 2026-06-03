from app.models.role import Role

def get_roles(db):
    return db.query(Role).all()

def create_role(db, name: str):
    role = Role(name=name)

    db.add(role)
    db.commit()
    db.refresh(role)

    return role