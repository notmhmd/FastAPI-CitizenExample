from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas

from .database import SessionLocal, engine

origin = [
    "http://localhost:4200"
]

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
app.add_middleware(CORSMiddleware,
                   allow_origins=origin,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/citizens/", response_model=schemas.Citizen)
def create_user(citizen: schemas.CitizenCreate, db: Session = Depends(get_db)):
    db_user = crud.get_citizen_by_national_id(db, nationality_id=citizen.nationality_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Citizen already registered")
    return crud.create_citizen(db=db, citizen=citizen)


@app.get("/citizens/", response_model=List[schemas.Citizen])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    citizens = crud.get_citizens(db, skip=skip, limit=limit)
    return citizens


@app.get("/citizens/{id}", response_model=schemas.Citizen)
def read_citizen(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_citizen(db, citizen_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Citizen not found")
    return db_user
