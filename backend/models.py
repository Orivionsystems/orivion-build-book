from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    """Represents a unit of work to be processed by an agent."""

    id: int
    description: str
    assigned_agent: Optional[str] = None


class TaskCreate(BaseModel):
    """Schema used for creating a new task via the API."""

    description: str
    assigned_agent: Optional[str] = None


class MemoryItem(BaseModel):
    """Represents an item stored in the memory system."""
    id: int
    content: str

class MemoryCreate(BaseModel):
    """Schema used for creating a new memory item via the API."""
    content: str
