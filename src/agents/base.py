class BaseAgent:
    """
    Abstract base class for AI agents.
    Each agent must implement the `run` method.
    """

    def __init__(self, name: str):
        self.name = name

    def run(self, *args, **kwargs):
        raise NotImplementedError("Agents must implement the 'run' method.")
