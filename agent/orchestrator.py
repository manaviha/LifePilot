from tasks.models import Goal, Task
from agent.models import AgentAction


class LifePilotOrchestrator:

    def __init__(self, goal):
        self.goal = goal

    # -----------------------------------------
    # GET ALL TASKS
    # -----------------------------------------

    def get_tasks(self):

        return Task.objects.filter(
            goal=self.goal
        ).order_by("created_at")


    # -----------------------------------------
    # GET CURRENT STATUS
    # -----------------------------------------

    def get_status(self):

        tasks = self.get_tasks()

        return {
            "total": tasks.count(),

            "completed": tasks.filter(
                status="completed"
            ).count(),

            "pending": tasks.filter(
                status="pending"
            ).count(),

            "blocked": tasks.filter(
                status="blocked"
            ).count(),
        }


    # -----------------------------------------
    # LOG AGENT ACTION
    # -----------------------------------------

    def log_action(
        self,
        action_type,
        action,
        reason=""
    ):

        return AgentAction.objects.create(
            goal=self.goal,
            action_type=action_type,
            action=action,
            reason=reason,
            success=True
        )


    # -----------------------------------------
    # DECIDE WHAT TO DO
    # -----------------------------------------

    def decide_next_action(self):

        status = self.get_status()

        if status["blocked"] > 0:

            self.log_action(
                "decision",
                "Replanning required",
                "The goal contains blocked tasks"
            )

            return "replan"


        if status["pending"] > 0:

            self.log_action(
                "decision",
                "Continue pending tasks",
                "The goal has pending tasks"
            )

            return "continue"


        if (
            status["total"] > 0
            and status["completed"] == status["total"]
        ):

            self.log_action(
                "verification",
                "Goal completed",
                "All tasks have been completed"
            )

            return "completed"


        return "no_action"


    # -----------------------------------------
    # EXECUTE NEXT ACTION
    # -----------------------------------------

    def execute_next_action(self):

        decision = self.decide_next_action()


        # -------------------------------------
        # CASE 1: CONTINUE
        # -------------------------------------

        if decision == "continue":

            next_task = self.get_tasks().filter(
                status="pending"
            ).first()


            if next_task:

                next_task.status = "in_progress"
                next_task.save()


                self.log_action(
                    "execute",
                    f"Started task: {next_task.title}",
                    "The orchestrator selected the next pending task"
                )


                return {
                    "decision": "continue",
                    "task": next_task.title
                }


        # -------------------------------------
        # CASE 2: REPLAN
        # -------------------------------------

        if decision == "replan":

            self.log_action(
                "replan",
                "Replanning required",
                "Blocked tasks require a new plan"
            )


            return {
                "decision": "replan"
            }


        # -------------------------------------
        # CASE 3: COMPLETED
        # -------------------------------------

        if decision == "completed":

            self.goal.status = "completed"
            self.goal.save()


            self.log_action(
                "verification",
                "Goal marked as completed",
                "All tasks are completed"
            )


            return {
                "decision": "completed"
            }


        # -------------------------------------
        # NO ACTION
        # -------------------------------------

        return {
            "decision": "no_action"
        }