from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_goal():
    return {"goal": "This is the goal route."}
