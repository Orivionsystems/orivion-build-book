class BaseAgent:
    """
    Base class for all ORIVION AI agents. Defines standard interface for initialization,
    processing tasks, and returning results.
    """

    def __init__(self, name: str, memory=None):
        self.name = name
        self.memory = memory

    async def setup(self):
        """Initialize any resources or context required by the agent."""
        pass

    async def process_task(self, task):
        """Process an incoming task and return a result. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement process_task")

    async def run(self, tasks):
        """Run the agent over an iterable of tasks, yielding results."""
        results = []
        for task in tasks:
            result = await self.process_task(task)
            results.append(result)
        return results
