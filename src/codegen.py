from pathlib import Path
from typing import Optional, List
import hashlib
import random
import time
from rich import print

# === Simulated Internal LLM Interface ===
class LocalModel:
    def generate(self, prompt: str, seed: Optional[int] = None) -> str:
        """Simulates generating code from an internal AI model."""
        random.seed(seed or time.time())
        variants = [
            "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello from Qwnt AI!'\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {\"message\": \"Welcome to Qwnt AI\"}\n",
            "import streamlit as st\n\nst.title('Qwnt AI Generator')\nst.write('Welcome to your new app.')"
        ]
        return random.choice(variants)


# === Quantum Sampler Logic ===
class QuantumSampler:
    def __init__(self, model: LocalModel, num_variants: int = 3):
        self.model = model
        self.num_variants = num_variants

    def sample(self, prompt: str) -> str:
        generations = [self.model.generate(prompt, seed=i) for i in range(self.num_variants)]
        scored = [(self._score_variant(g), g) for g in generations]
        scored.sort(reverse=True)
        return scored[0][1]

    def _score_variant(self, code: str) -> float:
        """Fake quantum scoring: entropy = length variance + hash entropy."""
        entropy = len(set(code)) / max(len(code), 1)
        hash_val = hashlib.sha256(code.encode()).hexdigest()
        hash_score = sum(ord(c) for c in hash_val[:10]) / 1000.0
        return entropy + hash_score


# === Code Generation Entry ===
def generate_code(prompt: str, output_dir: Optional[str] = None):
    print(f"[bold cyan]⚛️ CodeGen-AX initialized with quantum-enhanced sampling...[/bold cyan]")
    print(f"[bold green]🧠 Prompt:[/bold green] '{prompt}'\n")

    model = LocalModel()
    sampler = QuantumSampler(model)
    code = sampler.sample(prompt)

    output_path = Path(output_dir or "quill_output")
    output_path.mkdir(parents=True, exist_ok=True)
    file_path = output_path / "main.py"
    file_path.write_text(code)

    print(f"[green]✔ Code written to:[/green] {file_path.resolve()}")
    print("[bold green]\n✅ Generation complete. Ready to run or extend.\n[/bold green]")
