from typing import List

from fastapi import APIRouter, status

from .models import Task, TaskCreate
from agents.ceo_agent import CEOAgent

# Initialize router for task-related endpoints
router = APIRouter(prefix="/tasks", tags=["tasks"])

# In-memory store for tasks
_tasks_db: List[Task] = []

# Instantiate the CEO agent (in a real application this might be injected)
ceo_agent = CEOAgent()


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate) -> Task:
    """Create a new task and optionally delegate it to the appropriate agent.

    This function assigns a sequential ID to each task and appends it to an
    in-memory list. If the assigned_agent is not specified or is "CEOAgent",
    the task will be processed by the CEO agent.
    """
    task_id = len(_tasks_db) + 1
    task = Task(id=task_id, description=task_in.description, assigned_agent=task_in.assigned_agent)
    _tasks_db.append(task)

    # Delegate to the CEO agent by default or when explicitly requested
    if task.assigned_agent in (None, "CEOAgent"):
        ceo_agent.process_task({"id": task.id, "description": task.description})

    return task


@router.get("/", response_model=List[Task])
def list_tasks() -> List[Task]:
    """Return all created tasks."""
    return _tasks_db
