#@router.get("/")
#def get_task():
#    return {"task": "This is the task route."}

# app/routers/task.py

from fastapi import APIRouter
from app.models import Task, User
from typing import List
import random

router = APIRouter(prefix="/task", tags=["Task"])

tasks_db = []

@router.post("/generate", response_model=Task)
def generate_task(user: User):
    """根据角色属性生成一个 mock 任务"""
    task_id = len(tasks_db) + 1
    difficulty = random.choice(["easy", "medium", "hard"])

    task = Task(
        id=task_id,
        role_id=user.id,
        title=f"{user.name}的任务挑战",
        description=f"基于{user.personality}性格和技能{', '.join(user.skills)}，生成的{difficulty}难度任务。",
        difficulty=difficulty,
        tags=[user.personality] + user.skills
    )
    tasks_db.append(task)
    return task

@router.get("/", response_model=List[Task])
def get_all_tasks():
    return tasks_db
