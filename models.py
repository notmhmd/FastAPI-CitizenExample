from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Citizen(Base):
    __tablename__ = "citizen"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String)
    nationality_id = Column(String)
    phone_number = Column(String)
    state = Column(String)


