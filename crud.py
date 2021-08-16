from sqlalchemy.orm import Session

from . import models, schemas


def get_citizen(db: Session, citizen_id: int):
    return db.query(models.Citizen).filter(models.Citizen.id == citizen_id).first()


def get_citizen_by_national_id(db: Session, nationality_id: str):
    return db.query(models.Citizen).filter(models.Citizen.nationality_id == nationality_id).first()


def get_citizens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Citizen).offset(skip).limit(limit).all()


def create_citizen(db: Session, citizen: schemas.CitizenCreate):
    db_user = models.Citizen(nationality_id=citizen.nationality_id,
                             first_name=citizen.first_name,
                             last_name=citizen.last_name,
                             gender=citizen.last_name,
                             state=citizen.state,
                             phone_number=citizen.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
