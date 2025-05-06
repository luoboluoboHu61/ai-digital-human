# AI Digital Human Training (Backend)

A modular FastAPI backend for generating personalized training tasks based on user traits and goals.

Originally prototyped during an internship at ByteDance (Fall 2024), later refactored and extended into a modular, showcase-ready system (Spring 2025).

---

## Features

- Role system with attributes: personality, skills, goals
- Adaptive task generation based on user profile
- Modular structure: `user`, `goal`, `task`, `feedback`
- RESTful APIs with auto-generated docs at `/docs`


## Quick Start

```bash
git clone https://github.com/luoboluoboHu61/ai-digital-human.git
cd ai-digital-human

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Visit
API docs: http://127.0.0.1:8000/docs

Welcome route: http://127.0.0.1:8000/


## Project Structure
app/
├── main.py
├── models.py
└── routers/
    ├── user.py
    ├── goal.py
    ├── task.py
    └── feedback.py

PROJECT_LOG.md
README.md
requirements.txt

---

## Future Work
Add database integration for persistent role/task storage

Store and track user feedback and progress

Build frontend dashboard (React/Streamlit)

Deploy to Render / Hugging Face Spaces
