from fastapi import FastAPI, Form, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Profile
from schemas import UserProfileCreate, UserProfileUpdate
import os, shutil
from typing import List

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Persistent disk upload path
UPLOAD_DIR = "/opt/render/project/src/data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Mount uploads directory
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Register profile
@app.post("/profiles/register")
async def register_profile(
    name: str = Form(...),
    gender: str = Form(...),
    age: int = Form(...),
    marital_status: str = Form(...),
    caste: str = Form(...),
    city: str = Form(...),
    picture1: UploadFile = File(...),
    picture2: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Save pictures
    disk_path1 = os.path.join(UPLOAD_DIR, picture1.filename)
    disk_path2 = os.path.join(UPLOAD_DIR, picture2.filename)

    with open(disk_path1, "wb") as f1:
        shutil.copyfileobj(picture1.file, f1)
    with open(disk_path2, "wb") as f2:
        shutil.copyfileobj(picture2.file, f2)

    pic1_url = f"/uploads/{picture1.filename}"
    pic2_url = f"/uploads/{picture2.filename}"

    profile = Profile(
        name=name,
        gender=gender,
        age=age,
        marital_status=marital_status,
        caste=caste,
        city=city,
        picture1=pic1_url,
        picture2=pic2_url,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)
    return {"message": "Profile registered successfully!", "id": profile.id}

# GET all profiles
@app.get("/profiles", response_model=List[UserProfileCreate])
def get_all_profiles(db: Session = Depends(get_db)):
    return db.query(Profile).all()

# GET: View one profile (Admin)
@app.get("/profiles/{profile_id}")
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

# PUT: Update profile
@app.put("/profiles/{profile_id}")
def update_profile(profile_id: int, updated_data: UserProfileUpdate, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)
    return profile

# DELETE: Delete profile
@app.delete("/profiles/{profile_id}")
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    db.delete(profile)
    db.commit()
    return {"message": "Profile deleted"}
