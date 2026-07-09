from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.core.database import Base, engine
from app.models import Role, User, Category, Product, StockMovement, Sale, SaleItem, audit_log
from app.models.notifications import Notification
from app.routes.settings import router as settings_router
from app.routes import (
    auth,
    users,
    roles,
    products,
    stock_movements,
    inventory,
    sales,
    dashboard,
    reports,
    audit_log,
    category,
    notifications
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(notifications.router)
app.include_router(users.router)
app.include_router(roles.router)
app.include_router(inventory.router)
app.include_router(products.router)
app.include_router(category.router)
app.include_router(stock_movements.router)
app.include_router(sales.router)
app.include_router(audit_log.router)
app.include_router(reports.router)
app.include_router(settings_router)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

@app.get("/")
def root():
    return {"message": "SAIMS API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}