class BaseMemory:
    """
    Base class for ORIVION memory systems. Defines interface for storing and retrieving
    information using vector databases, knowledge graphs, or other backends.
    """

    async def store(self, item):
        """Store an item into memory."""
        raise NotImplementedError("Subclasses must implement store")

    async def retrieve(self, query, top_k: int = 10):
        """Retrieve relevant items given a query."""
        raise NotImplementedError("Subclasses must implement retrieve")

    async def search(self, query, top_k: int = 10):
        """Search the memory for items matching the query. By default calls retrieve."""
        return await self.retrieve(query, top_k=top_k)
