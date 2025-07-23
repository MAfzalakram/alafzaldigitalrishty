# app/models.py
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Profile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String)
    name = Column(String)
    age = Column(Integer)
    marital_status = Column(String)
    height = Column(String)
    qualification = Column(String)
    job_business = Column(String)
    income = Column(String)
    religion = Column(String)
    sect = Column(String)
    caste = Column(String)
    home_status = Column(String)
    house_size = Column(String)
    city = Column(String)
    address = Column(String)
    nationality = Column(String)
    father_occupation = Column(String)
    mother_occupation = Column(String)
    siblings = Column(String)
    married_siblings = Column(String)
    requirement_age = Column(String)
    requirement_height = Column(String)
    requirement_city = Column(String)
    requirement_caste = Column(String)
    requirement_qualification = Column(String)
    picture1 = Column(String)
    picture2 = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
