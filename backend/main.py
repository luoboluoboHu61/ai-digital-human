# backend/main.py


from fastapi import FastAPI
from app.routers import user, goal, task, feedback

app = FastAPI(title="AI Digital Human Training System")

# 注册各路由模块
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(goal.router, prefix="/goal", tags=["Goal"])
app.include_router(task.router, prefix="/task", tags=["Task"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Digital Human Training System"}

