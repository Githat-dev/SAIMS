from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import Role, User

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SAIMS API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}