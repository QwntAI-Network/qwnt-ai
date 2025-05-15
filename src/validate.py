from pathlib import Path
from typing import Optional
from rich import print
from pipeline import run_pipeline
import json
import yaml
import subprocess

# === SYN-VAL/42 Engine ===
class SchemaValidator:
    def __init__(self, file_path: str):
        self.file = Path(file_path)
        self.ext = self.file.suffix.lower()

    def validate(self):
        if not self.file.exists():
            print(f"[red]✖ File not found: {self.file}[/red]")
            return

        try:
            if self.ext in [".json"]:
                self._validate_json()
            elif self.ext in [".yaml", ".yml"]:
                self._validate_yaml()
            elif self.ext in [".html", ".xml"]:
                self._validate_lint()
            else:
                print(f"[yellow]⚠ Unsupported file type for validation: {self.ext}[/yellow]")
        except Exception as e:
            print(f"[red]✖ Validation error: {e}[/red]")

    def _validate_json(self):
        print("[blue]🔍 Validating JSON structure...[/blue]")
        with self.file.open("r") as f:
            json.load(f)
        print("[green]✔ JSON is valid.[/green]")

    def _validate_yaml(self):
        print("[blue]🔍 Validating YAML structure...[/blue]")
        with self.file.open("r") as f:
            yaml.safe_load(f)
        print("[green]✔ YAML is valid.[/green]")

    def _validate_lint(self):
        print("[blue]🔍 Running external linter...[/blue]")
        result = subprocess.run(["tidy", "-q", str(self.file)], capture_output=True, text=True)
        if result.returncode == 0:
            print("[green]✔ Markup is clean.[/green]")
        else:
            print(f"[yellow]⚠ Markup issues found:[/yellow]\n{result.stderr.strip()}")


# === DX-Pipeline CLI Mode ===
def run_ci_pipeline():
    print("[bold cyan]🧪 Running test and validation pipeline (DX-Pipeline)...[/bold cyan]")
    result = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
    print(result.stdout if result.returncode == 0 else result.stderr)
    print("[green]✔ Pipeline complete.[/green]" if result.returncode == 0 else "[red]✖ Pipeline failed.[/red]")


# === CLI Entry ===
def validate_file(file: str, ci: bool = False):
    if ci:
        run_pipeline()
    else:
        validator = SchemaValidator(file)
        validator.validate()