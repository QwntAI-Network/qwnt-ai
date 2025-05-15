import subprocess
from rich import print
from pathlib import Path

# === DX-Pipeline (Test + Lint + Type Check Runner) ===
def run_pipeline():
    print("[bold cyan]🔁 DX-Pipeline: Full validation cycle starting...[/bold cyan]\n")

    results = {
        "tests": _run_pytest(),
        "types": _run_mypy(),
        "lint": _run_flake8()
    }

    success = all(results.values())
    print("\n[bold green]✅ Pipeline complete![/bold green]" if success else "\n[red]❌ One or more steps failed.[/red]")


def _run_pytest() -> bool:
    print("[blue]🧪 Running unit tests with pytest...[/blue]")
    result = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
    print(result.stdout)
    return result.returncode == 0


def _run_mypy() -> bool:
    print("[blue]🔎 Type-checking with mypy...[/blue]")
    result = subprocess.run(["mypy", "src/"], capture_output=True, text=True)
    print(result.stdout)
    return result.returncode == 0


def _run_flake8() -> bool:
    print("[blue]🎯 Linting with flake8...[/blue]")
    result = subprocess.run(["flake8", "src/"], capture_output=True, text=True)
    print(result.stdout or "[green]✔ No linting issues found.[/green]")
    return result.returncode == 0
