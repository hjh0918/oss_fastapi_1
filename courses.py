import json
from fastapi import APIRouter
from model import Course

courses_router = APIRouter()

DATA_FILE = "courses.json"

def read_courses():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_courses(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@courses_router.get("/courses")
async def get_courses() -> dict:
    data = read_courses()
    return {"courses": data}


@courses_router.post("/courses")
async def add_course(course: Course) -> dict:
    data = read_courses()
    data.append(course.dict())
    write_courses(data)
    return {"msg": "course added successfully"}