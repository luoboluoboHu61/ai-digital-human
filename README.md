
# AI Digital Human Training (Backend)

A modular FastAPI backend for generating personalized training tasks based on user traits and goals.

---

## Features

- Role system with attributes: personality, skills, goals
- Adaptive task generation based on user profile
- Modular structure: `user`, `goal`, `task`, `feedback`
- RESTful APIs with auto docs at `/docs`

---

## Quick Start

```bash
git clone https://github.com/luoboluoboHu61/ai-digital-human.git
cd ai-digital-human

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload


Docs available at: http://127.0.0.1:8000/docs


## Project Structure
```app/
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

## Future Work
```Add database integration

Save user progress and feedback

Build frontend dashboard

