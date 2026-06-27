from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    naem: str | None = None

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True