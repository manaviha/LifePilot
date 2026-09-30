# 🚀 LifePilot

## Autonomous AI Goal-Execution Agent

> **Autonomous when safe. Human-controlled when important.**

LifePilot is an AI-powered autonomous goal-execution assistant that converts high-level user goals into actionable tasks, monitors progress, makes decisions, and dynamically replans when tasks are blocked.

Unlike a traditional task manager, LifePilot doesn't just store tasks. It uses an **agentic workflow** to understand goals, create plans, decide what to do next, execute actions, verify progress, and adapt when circumstances change.

---

## 🎯 Problem

People often know what they want to achieve but struggle to:

- Break large goals into practical tasks
- Decide what to do next
- Adapt when a task becomes blocked
- Maintain progress toward the original goal

Traditional task managers mainly organize tasks but do not autonomously adapt the plan.

---

## 💡 Solution

LifePilot uses **Google Gemini + an autonomous orchestrator** to transform goals into dynamic action plans.

### Agentic Workflow

```text
User Goal
    ↓
Understand
    ↓
Generate Plan
    ↓
Analyze Task State
    ↓
Make Decision
    ↓
Execute
    ↓
Verify
    ↓
Replan if Required
```

---

## 🤖 Key Features

### 1. AI Goal Planning

The user enters a high-level goal such as:

```text
Prepare for my DBMS viva
```

Gemini automatically generates practical tasks.

### 2. Autonomous Decision Engine

LifePilot analyzes the current state and decides what should happen next.

| Task State | Agent Decision |
|---|---|
| Blocked tasks exist | REPLAN |
| Pending tasks exist | CONTINUE |
| All tasks completed | COMPLETED |

### 3. Autonomous Task Execution

When the agent decides to continue, it automatically selects the next pending task and changes its state:

```text
Pending → In Progress
```

### 4. Dynamic Replanning

If a task becomes blocked, LifePilot asks Gemini to generate alternative tasks instead of stopping.

```text
Blocked Task
     ↓
Analyze Situation
     ↓
Gemini
     ↓
Generate Replacement Tasks
     ↓
Continue Goal
```

### 5. Agent Activity Log

The system records important agent actions including:

- Planning
- Decisions
- Execution
- Replanning
- Verification

This makes the agent's actions visible to the user.

---

## 🧠 System Architecture

```text
                 USER
                   │
                   ▼
              GOAL INPUT
                   │
                   ▼
          ┌─────────────────┐
          │ Gemini Planner  │
          └────────┬────────┘
                   │
                   ▼
              TASK PLAN
                   │
                   ▼
        ┌─────────────────────┐
        │ LifePilot           │
        │ Orchestrator        │
        └──────────┬──────────┘
                   │
             Analyze State
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     REPLAN     CONTINUE   COMPLETED
        │          │          │
        ▼          ▼          ▼
     Gemini     Execute     Verify
     Replan      Task        Goal
        │          │          │
        └──────────┼──────────┘
                   ▼
            Agent Activity Log
                   │
                   ▼
               Database
```

---

## 🔄 Autonomous Decision Logic

```text
              Check Goal
                  │
                  ▼
          Are tasks blocked?
             /          \
           YES           NO
            │             │
            ▼             ▼
         REPLAN      Are tasks pending?
                       /        \
                     YES         NO
                      │           │
                      ▼           ▼
                   CONTINUE   All completed?
                                  │
                                  ▼
                              COMPLETED
```

---

## 🛠️ Technology Stack

### Backend
- Python
- Django 6.1.1

### AI
- Google Gemini API
- `google-genai`

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

### Development Tools
- VS Code
- Git
- GitHub
- Python Virtual Environment

---

## 📂 Project Structure

```text
LifePilot/
│
├── agent/
│   ├── gemini_service.py
│   ├── models.py
│   ├── orchestrator.py
│   ├── views.py
│   └── migrations/
│
├── core/
│   ├── views.py
│   ├── models.py
│   └── migrations/
│
├── tasks/
│   ├── models.py
│   ├── views.py
│   └── migrations/
│
├── lifepilot/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   └── home.html
│
├── manage.py
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manaviha/LifePilot.git
cd LifePilot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

For Windows CMD:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install django
pip install google-genai
pip install python-dotenv
```

### 5. Configure Gemini API

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

**Never upload your actual Gemini API key to GitHub.**

The `.gitignore` file excludes `.env`.

### 6. Run Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Application

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Example

### User Goal

```text
Prepare for my DBMS viva
```

### AI Planning

Gemini generates multiple practical tasks based on the goal.

### User Blocks a Task

```text
BLOCKED
```

### LifePilot Decision

```text
REPLAN
```

### Gemini Replanning

Gemini generates replacement or adjusted tasks that help the user continue toward the original goal.

---

## 🧩 Agent Execution Example

When a goal contains pending tasks:

```text
Goal
 ↓
Check Task State
 ↓
Pending Task Found
 ↓
Select Next Task
 ↓
Change Status
Pending → In Progress
 ↓
Log Agent Action
```

The orchestrator performs this using the actual task data stored in the database.

---

## 📊 Agent Actions

LifePilot maintains an activity history for important agent operations.

Examples include:

```text
PLAN
Created initial task plan

DECISION
Continue pending tasks

EXECUTE
Started task

REPLAN
Generated replacement tasks

VERIFICATION
Goal completed
```

This provides transparency into the agent's actions.

---

## 🔐 Security

The following files are excluded from Git:

```text
.env
venv/
__pycache__/
*.pyc
db.sqlite3
```

The Gemini API key is stored in `.env` and is not included in the repository.

**Never commit or publicly share your API key.**

---

## 🚀 Future Enhancements

Planned improvements include:

- Human Approval Gateway
- Multi-Agent Architecture
- What-If Plan Simulator
- Agent Performance Dashboard
- Deadline Risk Prediction
- Long-Term Agent Memory
- Calendar Integration
- Voice Interaction
- MCP Tool Integration
- PostgreSQL Support
- Cloud Deployment

---

## 🏆 Vision

LifePilot aims to move productivity applications from:

```text
Task Management
       ↓
AI Assistance
       ↓
Autonomous Goal Execution
```

The long-term vision is an AI agent that can understand goals, create plans, take actions, verify outcomes, and adapt its strategy while keeping the user in control of important decisions.

---

## 👩‍💻 Author

**Manavi H A**

GitHub:  
https://github.com/manaviha

---

## 📜 License

This project is developed for educational, research, and hackathon purposes.
