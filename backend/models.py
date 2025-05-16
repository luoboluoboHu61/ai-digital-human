# backend/models.py

from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    gender: str
    personality: str
    skills: List[str]
    description: str

class Task(BaseModel):
    id: int
    role_id: int
    title: str
    description: str
    difficulty: str  # "easy" | "medium" | "hard"
    tags: List[str]

# app/models.py

class Goal(BaseModel):
    id: int
    role_id: int
    content: str
    deadline: str  # 你也可以用 datetime 类型

class Feedback(BaseModel):
    id: int
    task_id: int
    role_id: int
    rating: int  # 1~5 分
    comment: str
