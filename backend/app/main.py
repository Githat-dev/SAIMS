from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import Role, User
from app.routes import auth, users, roles

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(roles.router)

@app.get("/")
def root():
    return {"message": "SAIMS API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}