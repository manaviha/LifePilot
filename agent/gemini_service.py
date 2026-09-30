import os

from dotenv import load_dotenv
from google import genai


# Load variables from .env
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Create Gemini client
client = genai.Client(api_key=api_key)


# --------------------------------------------------
# Generate tasks for a new goal
# --------------------------------------------------

def generate_tasks(goal):

    prompt = f"""
You are LifePilot, an AI goal-planning assistant.

The user has given this goal:

{goal}

Break this goal into 4 practical tasks.

Return ONLY the task names.
Put each task on a separate line.
Do not number them.
Do not add explanations.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


# --------------------------------------------------
# Replan when a task is blocked
# --------------------------------------------------

def replan_tasks(goal, blocked_task, remaining_tasks):

    prompt = f"""
You are LifePilot, an autonomous goal-planning agent.

The user's main goal is:

{goal}

One task has been blocked:

{blocked_task}

Other remaining tasks are:

{remaining_tasks}

Create 3 practical replacement or adjusted tasks
that help the user continue toward the original goal.

Consider the blocked task and avoid simply repeating it.

Return ONLY the task names.
Put each task on a separate line.
Do not number them.
Do not add explanations.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text