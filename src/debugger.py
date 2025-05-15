import subprocess
from pathlib import Path
from typing import List
from rich import print

# === Debugger Engine (Simulates SYN-VAL/42) ===
class CodeDebugger:
    def __init__(self, path: str):
        self.path = Path(path)

    def run_linters(self) -> None:
        print("[bold blue]🧪 Running static analysis...[/bold blue]")
        self._run_command(["flake8", str(self.path)])

    def run_formatter_check(self) -> None:
        print("[bold blue]🎯 Checking code style...[/bold blue]")
        self._run_command(["black", "--check", str(self.path)])

    def run_type_checks(self) -> None:
        print("[bold blue]🔎 Running type checks...[/bold blue]")
        self._run_command(["mypy", str(self.path)])

    def summarize_findings(self) -> None:
        print("\n[bold green]✅ Debugging complete. Review logs above for issues or inconsistencies.[/bold green]")

    def _run_command(self, command: List[str]) -> None:
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"[green]✔ {command[0]} passed[/green]")
            else:
                print(f"[yellow]⚠ {command[0]} issues found:[/yellow]\n{result.stdout}")
        except FileNotFoundError:
            print(f"[red]✖ Tool not found: {command[0]}. Please install it.[/red]")

# === CLI Entry Function ===
def debug_code(path: str):
    debugger = CodeDebugger(path)
    debugger.run_linters()
    debugger.run_formatter_check()
    debugger.run_type_checks()
    debugger.summarize_findings()