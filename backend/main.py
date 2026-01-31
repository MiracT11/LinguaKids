from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from models import User
from schemas import UserCreate, UserResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LinguaKids API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "LinguaKids backend çalışıyor 🎉"}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        level=1,
        total_score=0
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
