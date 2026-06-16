from typing import List, Dict, Any

from .base_memory import BaseMemory


class InMemoryMemory(BaseMemory):
    """
    A simple in-memory implementation of the BaseMemory interface. This class
    stores items in a list of dictionaries and provides basic retrieval and
    search functionality. It is suitable for prototyping and small-scale
    applications but should be replaced with a persistent vector database or
    knowledge graph in production.
    """

    def __init__(self) -> None:
        super().__init__()
        self.data: List[Dict[str, Any]] = []

    def store(self, item: Dict[str, Any]) -> None:
        """Store an item in memory."""
        self.data.append(item)

    def retrieve(self, identifier: str) -> Dict[str, Any] | None:
        """Retrieve an item by its identifier."""
        for item in self.data:
            if item.get("id") == identifier:
                return item
        return None

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Perform a simple case-insensitive search over stored items."""
        results: List[Dict[str, Any]] = []
        query_lower = query.lower()
        for item in self.data:
            # Convert the item to a string for naive substring search
            if query_lower in str(item).lower():
                results.append(item)
        return results
