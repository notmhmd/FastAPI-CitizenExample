from typing import List, Optional

from pydantic import BaseModel


class CitizenBase(BaseModel):
    nationality_id: str
    first_name: str
    last_name: str
    phone_number: str
    gender: str
    state: str


class CitizenCreate(CitizenBase):
    nationality_id: str
    first_name: str
    last_name: str
    phone_number: str
    gender: str
    state: str



class Citizen(CitizenBase):
    id: int

    class Config:
        orm_mode = True
