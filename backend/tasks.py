from typing import List
from fastapi import APIRouter, status

from .models import Task, TaskCreate
from agents.ceo_agent import CEOAgent
from agents.research_agent import ResearchAgent

# Initialize router for task-related endpoints
router = APIRouter(prefix="/tasks", tags=["tasks"])

# In-memory store for tasks
_tasks_db: List[Task] = []

# Instantiate the agents (in a real application these might be injected)
ceo_agent = CEOAgent()
research_agent = ResearchAgent()


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate) -> Task:
    """Create a new task and optionally delegate it to the appropriate agent."""

    task_id = len(_tasks_db) + 1
    task = Task(id=task_id, description=task_in.description, assigned_agent=task_in.assigned_agent)
    _tasks_db.append(task)

    # Delegate processing to the appropriate agent
    if task.assigned_agent is None or task.assigned_agent == CEOAgent.__name__:
        ceo_agent.process_task(task.description)
    elif task.assigned_agent == ResearchAgent.__name__:
        research_agent.process_task(task.description)
    else:
        # Unknown agent; could log or handle unsupported agents here
        pass

    return task


@router.get("/", response_model=List[Task])
def list_tasks() -> List[Task]:
    """Return all created tasks."""
    return _tasks_db
