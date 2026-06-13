from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import Role, User, Category, Product, StockMovement, Sale, SaleItem
from app.routes import auth, users, roles, products, stock_movements, inventory, sales, dashboard, reports

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(roles.router)
app.include_router(products.router)
app.include_router(stock_movements.router)
app.include_router(inventory.router)
app.include_router(sales.router)
app.include_router(dashboard.router)
app.include_router(reports.router)


@app.get("/")
def root():
    return {"message": "SAIMS API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}