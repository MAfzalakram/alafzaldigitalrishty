from typing import Optional
from pydantic import BaseModel

class UserProfileCreate(BaseModel):
    id: int
    name: str
    gender: str
    age: int
    marital_status: str
    caste: str
    city: str
    picture1: str
    picture2: str

    # The rest should be Optional[str]
    height: Optional[str] = None
    qualification: Optional[str] = None
    job_business: Optional[str] = None
    income: Optional[str] = None
    religion: Optional[str] = None
    sect: Optional[str] = None
    home_status: Optional[str] = None
    house_size: Optional[str] = None
    address: Optional[str] = None
    nationality: Optional[str] = None
    father_occupation: Optional[str] = None
    mother_occupation: Optional[str] = None
    siblings: Optional[str] = None
    married_siblings: Optional[str] = None
    requirement_height: Optional[str] = None
    requirement_caste: Optional[str] = None
    requirement_qualification: Optional[str] = None

    class Config:
        orm_mode = True

class UserProfileUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    marital_status: Optional[str] = None
    caste: Optional[str] = None
    city: Optional[str] = None
    picture1: Optional[str] = None
    picture2: Optional[str] = None

    height: Optional[str] = None
    qualification: Optional[str] = None
    job_business: Optional[str] = None
    income: Optional[str] = None
    religion: Optional[str] = None
    sect: Optional[str] = None
    home_status: Optional[str] = None
    house_size: Optional[str] = None
    address: Optional[str] = None
    nationality: Optional[str] = None
    father_occupation: Optional[str] = None
    mother_occupation: Optional[str] = None
    siblings: Optional[str] = None
    married_siblings: Optional[str] = None
    requirement_height: Optional[str] = None
    requirement_caste: Optional[str] = None
    requirement_qualification: Optional[str] = None

    class Config:
        orm_mode = True
