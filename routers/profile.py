from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
import models, schemas, database
import shutil
import uuid
import os

router = APIRouter(prefix="/profiles", tags=["Profiles"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/register")
async def register_profile(
    gender: str = Form(...),
    name: str = Form(...),
    age: int = Form(...),
    marital_status: str = Form(...),
    height: str = Form(...),
    qualification: str = Form(...),
    job_business: str = Form(...),
    income: str = Form(...),
    religion: str = Form(...),
    sect: str = Form(...),
    caste: str = Form(...),
    home_status: str = Form(...),
    house_size: str = Form(...),
    city: str = Form(...),
    address: str = Form(...),
    nationality: str = Form(...),
    father_occupation: str = Form(...),
    mother_occupation: str = Form(...),
    siblings: str = Form(...),
    married_siblings: str = Form(...),
    requirement_age: str = Form(...),
    requirement_height: str = Form(...),
    requirement_city: str = Form(...),
    requirement_caste: str = Form(...),
    requirement_qualification: str = Form(...),
    picture1: UploadFile = File(...),
    picture2: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    def save_image(file: UploadFile):
        ext = file.filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_path

    pic1_path = save_image(picture1)
    pic2_path = save_image(picture2)

    new_profile = models.UserProfile(
        gender=gender,
        name=name,
        age=age,
        marital_status=marital_status,
        height=height,
        qualification=qualification,
        job_business=job_business,
        income=income,
        religion=religion,
        sect=sect,
        caste=caste,
        home_status=home_status,
        house_size=house_size,
        city=city,
        address=address,
        nationality=nationality,
        father_occupation=father_occupation,
        mother_occupation=mother_occupation,
        siblings=siblings,
        married_siblings=married_siblings,
        requirement_age=requirement_age,
        requirement_height=requirement_height,
        requirement_city=requirement_city,
        requirement_caste=requirement_caste,
        requirement_qualification=requirement_qualification,
        picture1=pic1_path,
        picture2=pic2_path
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return {"message": "Profile registered successfully", "id": new_profile.id}
