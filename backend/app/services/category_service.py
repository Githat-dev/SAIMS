from app.models.category import Category

def get_all_categories(db):
    return db.query(Category).all()

def get_category_by_id(
        db,
        category_id: int
):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db, category):
    new_category = Category(**category.model_dump())

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def update_category(
        db,
        category_id: int,
        category
):
    db_category = get_category_by_id(db, category_id)

    if not db_category:
        return None
    
    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)

        db.commit()
        db.refresh(db_category)

        return db_category
    
def delete_category(
        db,
        category_id: int
):
    db_category = get_category_by_id(db, category_id)

    if not db_category:
        return None
    
    db.delete(db_category)
    db.commit()

    return {"message": "Category deleted successfully"}