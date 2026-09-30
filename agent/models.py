from django.db import models
from tasks.models import Goal, Task


class AgentAction(models.Model):
    ACTION_TYPES = [
        ("plan", "Plan"),
        ("execute", "Execute"),
        ("replan", "Replan"),
        ("research", "Research"),
        ("decision", "Decision"),
        ("verification", "Verification"),
    ]

    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name="agent_actions"
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agent_actions"
    )

    action_type = models.CharField(
        max_length=30,
        choices=ACTION_TYPES
    )

    action = models.CharField(max_length=255)

    reason = models.TextField(blank=True)

    success = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type}: {self.action}"