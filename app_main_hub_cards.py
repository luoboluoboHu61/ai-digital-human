import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="AI Digital Human Hub", layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
<style>
.card-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background-color: #f9f9f9;
    border-radius: 12px;
    padding: 1rem;
    max-width: 260px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.card-button {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 10px;
    border: none;
    background-color: #ffffff;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.card-button:hover {
    background-color: #e8e8e8;
}
.card-button.selected {
    background-color: #d1e7ff;
}
.view-score-button {
    padding: 0.75rem 1rem;
    margin-top: 0.5rem;
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    width: 100%;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar/Card Style Navigation Area ---
st.sidebar.markdown("## 🗂️ Main Menu")

# Session state for active module
if "active_module" not in st.session_state:
    st.session_state.active_module = "🏠 Home"

# Buttons as cards
def card_button(label, icon, key):
    if st.sidebar.button(f"{icon} {label}", key=key):
        st.session_state.active_module = label

card_button("🏠 Home", "", "home_btn")
card_button("👤 Create Character", "", "create_char_btn")
card_button("🧠 Generate Task", "", "gen_task_btn")
card_button("✉️ Submit Feedback", "", "submit_feedback_btn")
card_button("📊 View Score", "", "view_score_btn")

# --- Shared Data ---
TASK_FILE = "task_data.json"
FEEDBACK_FILE = "feedback_data.json"

if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        task_data = json.load(f)
else:
    task_data = {}

if os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
        feedback_data = json.load(f)
else:
    feedback_data = {}

# --- Dynamic Main Area ---
st.title(f"📍 {st.session_state.active_module}")

if st.session_state.active_module == "🏠 Home":
    st.markdown("Welcome to the AI Digital Human Bootcamp Dashboard. Select a function from the menu.")

elif st.session_state.active_module == "👤 Create Character":
    role = st.selectbox("Choose your role", ["User", "Mentor", "Admin"])
    st.success(f"Character role set to: {role}")

elif st.session_state.active_module == "🧠 Generate Task":
    if task_data:
        st.markdown("### Task List")
        for name, info in task_data.items():
            st.markdown(f"**{name}**: {info['desc']} | {'✅ Completed' if info['completed'] else '⏳ In Progress'}")
    else:
        st.info("No tasks available.")

elif st.session_state.active_module == "✉️ Submit Feedback":
    if task_data:
        selected_task = st.selectbox("Select Task", list(task_data.keys()))
        score = st.slider("Score", 1, 10, 5)
        comment = st.text_area("Comment")
        if st.button("Submit"):
            if selected_task not in feedback_data:
                feedback_data[selected_task] = []
            feedback_data[selected_task].append({
                "score": score,
                "comment": comment,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
                json.dump(feedback_data, f, ensure_ascii=False, indent=2)
            st.success("Feedback submitted successfully.")
    else:
        st.warning("No tasks found to review.")

elif st.session_state.active_module == "📊 View Score":
    if feedback_data:
        for task, records in feedback_data.items():
            st.markdown(f"## 📌 Task: {task}")
            for r in records:
                st.markdown(f"- Score: **{r['score']}**, Comment: {r['comment']}, Time: {r['timestamp']}")
    else:
        st.info("No feedback submitted yet.")