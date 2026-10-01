from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from tasks.models import Goal, Task
from agent.models import AgentAction

from agent.gemini_service import generate_tasks, replan_tasks


def home(request):

    if request.method == "POST":

        goal_text = request.POST.get("goal")

        if goal_text:

            # Get or create a demo user
            user, created = User.objects.get_or_create(
                username="lifepilot_demo"
            )

            # Create the goal
            goal = Goal.objects.create(
                user=user,
                title=goal_text
            )

            # Generate initial tasks using Gemini
            ai_tasks = generate_tasks(goal_text)

            task_list = ai_tasks.strip().split("\n")

            for task_title in task_list:

                task_title = task_title.strip()

                if task_title:
                    Task.objects.create(
                        goal=goal,
                        title=task_title
                    )

            # Log planning action
            AgentAction.objects.create(
                goal=goal,
                action_type="plan",
                action="Created initial task plan",
                reason="Gemini generated tasks from the user's goal",
                success=True
            )

        return redirect("home")


    # Get or create the demo user
    user, created = User.objects.get_or_create(
        username="lifepilot_demo"
    )

    # Get active goals
    goals = Goal.objects.filter(
        user=user,
        status="active"
    ).order_by("-created_at")


    # Get recent agent activity
    agent_actions = AgentAction.objects.select_related(
        "goal",
        "task"
    ).order_by("-created_at")[:20]


    return render(
        request,
        "home.html",
        {
            "goals": goals,
            "agent_actions": agent_actions
        }
    )


def complete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.status = "completed"
    task.save()


    # Log task completion
    AgentAction.objects.create(
        goal=task.goal,
        task=task,
        action_type="execute",
        action="Completed task",
        reason="User marked the task as completed",
        success=True
    )


    return redirect("home")


def block_task(request, task_id):

    task = Task.objects.get(id=task_id)

    # Mark task as blocked
    task.status = "blocked"
    task.save()

    goal = task.goal


    # Get other unfinished tasks
    remaining_tasks = Task.objects.filter(
        goal=goal
    ).exclude(
        status="completed"
    ).exclude(
        id=task.id
    )


    # Convert remaining tasks into text
    remaining_text = "\n".join(
        f"- {t.title} ({t.status})"
        for t in remaining_tasks
    )


    # Ask Gemini to replan
    new_tasks_text = replan_tasks(
        goal.title,
        task.title,
        remaining_text
    )


    # Convert Gemini response into individual tasks
    new_task_list = new_tasks_text.strip().split("\n")


    for task_title in new_task_list:

        task_title = task_title.strip()

        if task_title:
            Task.objects.create(
                goal=goal,
                title=task_title
            )


    # Log replanning action
    AgentAction.objects.create(
        goal=goal,
        task=task,
        action_type="replan",
        action="Generated replacement tasks",
        reason=f"Task blocked: {task.title}",
        success=True
    )


    return redirect("home")