from .base import BaseAgent
from pathlib import Path

class CodeReviewAgent(BaseAgent):
    """
    Agent that performs basic code reviews for readability and style.
    """

    def run(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            return f"[CodeReviewAgent:{self.name}] File not found: {file_path}"

        content = path.read_text()
        lines = content.splitlines()
        issues = []

        for i, line in enumerate(lines, start=1):
            if len(line) > 100:
                issues.append(f"Line {i} too long ({len(line)} chars)")
            if line.strip().startswith("print"):
                issues.append(f"Line {i} uses print(), consider logging")

        if not issues:
            return f"[CodeReviewAgent:{self.name}] No issues found."

        return f"[CodeReviewAgent:{self.name}] Found issues:\n- " + "\n- ".join(issues)
