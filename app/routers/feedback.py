#@router.get("/")
#def get_feedback():
#    return {"feedback": "This is the feedback route."}

# backend/routers/feedback.py

from fastapi import APIRouter
from app.models import Feedback
from typing import List

router = APIRouter(prefix="/feedback", tags=["Feedback"])

feedback_db = []

@router.post("/", response_model=Feedback)
def create_feedback(feedback: Feedback):
    feedback_db.append(feedback)
    return feedback

@router.get("/", response_model=List[Feedback])
def get_all_feedback():
    return feedback_db
