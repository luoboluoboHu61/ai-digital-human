# backend/routers/user.py
#@router.get("/profile")
#def get_profile():
#    return {"user": "test_user", "role": "Buddhist"}

# app/routers/user.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.models import User

router = APIRouter(prefix="/user", tags=["User"])

users_db = []

@router.post("/", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

@router.get("/", response_model=List[User])
def get_all_users():
    return users_db

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            del users_db[i]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

