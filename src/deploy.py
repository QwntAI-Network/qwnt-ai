from pathlib import Path
from rich import print
import shutil
import subprocess
import tempfile

# === Deployment Engine (Simulated for Firebase/Static Hosts) ===
class DeployEngine:
    def __init__(self, source_dir: str = "quill_output"):
        self.source = Path(source_dir)
        if not self.source.exists():
            raise FileNotFoundError(f"Deployment source directory '{self.source}' not found.")

    def deploy(self, target: str = "local"):
        print(f"[bold cyan]🚀 Starting deployment to:[/bold cyan] {target}\n")

        if target == "firebase":
            self._deploy_to_firebase()
        elif target == "vercel":
            self._deploy_to_vercel()
        elif target == "local":
            self._preview_locally()
        else:
            print(f"[red]✖ Unknown deployment target: {target}[/red]")

    def _deploy_to_firebase(self):
        # Simulated Firebase deployment
        print("[blue]Preparing Firebase project...[/blue]")
        subprocess.run(["firebase", "deploy", "--only", "hosting"], cwd=self.source)
        print("[green]✔ Firebase deployment initiated.[/green]")

    def _deploy_to_vercel(self):
        print("[blue]Pushing project to Vercel...[/blue]")
        subprocess.run(["vercel", "--prod"], cwd=self.source)
        print("[green]✔ Deployed with Vercel. Check your dashboard.[/green]")

    def _preview_locally(self):
        preview_path = self.source / "index.html"
        if preview_path.exists():
            print(f"[green]✔ You can preview the site by opening:[/green] {preview_path.resolve()}")
        else:
            print("[yellow]⚠ No index.html found to preview.[/yellow]")


# === CLI Entry ===
def deploy(target: str = "local"):
    engine = DeployEngine()
    engine.deploy(target)