from fastapi import FastAPI, UploadFile, File
from .face_detection import detect_student
from .food_detection import detect_food
from .nutrition import calculate_nutrition
from .database import save_record
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    student = detect_student(file_path)
    foods = detect_food(file_path)
    nutrition = calculate_nutrition(foods)
    meal_allocated = "Yes" if foods else "No"

    save_record(student, foods, nutrition)

    return {
        "student": student,
        "foods": foods,
        "nutrition": nutrition,
        "attendance": "Marked",
        "meal_allocated_today": meal_allocated
    }