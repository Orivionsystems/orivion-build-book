from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any

from .models import MemoryItem, MemoryCreate


router = APIRouter(prefix="/memory", tags=["memory"])

# In-memory storage for memory items
memory_data: List[Dict[str, Any]] = []
current_id = 1


@router.get("/", response_model=List[MemoryItem])
async def list_memory() -> List[MemoryItem]:
    """Return all memory items."""
    return memory_data


@router.post("/", response_model=MemoryItem, status_code=status.HTTP_201_CREATED)
async def create_memory(item: MemoryCreate) -> MemoryItem:
    """Create a new memory item."""
    global current_id
    mem_item = {"id": current_id, "content": item.content}
    memory_data.append(mem_item)
    current_id += 1
    return mem_item  # type: ignore[return-value]


@router.get("/{item_id}", response_model=MemoryItem)
async def get_memory(item_id: int) -> MemoryItem:
    """Retrieve a memory item by its ID."""
    for mem in memory_data:
        if mem["id"] == item_id:
            return mem  # type: ignore[return-value]
    raise HTTPException(status_code=404, detail="Memory item not found")


@router.get("/search/", response_model=List[MemoryItem])
async def search_memory(query: str, top_k: int = 5) -> List[MemoryItem]:
    """Search memory items by query, returning top_k matches."""
    results = [mem for mem in memory_data if query.lower() in mem["content"].lower()]
    return results[:top_k]
