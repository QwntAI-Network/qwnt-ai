from .base import BaseAgent

class ChatAgent(BaseAgent):
    """
    Agent that simulates AI chat interaction.
    """

    def run(self, prompt: str) -> str:
        return f"[ChatAgent:{self.name}] Response to: '{prompt}'"
