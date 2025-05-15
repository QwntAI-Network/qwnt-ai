import typer
from rich import print
from codegen import generate_code
from debugger import debug_code
from uigen import generate_ui
from translate import translate
from validate import validate_file
from mentor import mentor
from visualizer import visualize
from deploy import deploy as deploy_cmd

# Initialize Typer app
app = typer.Typer(help="Qwnt AI - The Quantum-Enhanced AI CLI Toolkit")

@app.command()
def generate(prompt: str = typer.Argument(..., help="Prompt describing the application or code to generate.")):
    """Generate code from natural language prompts."""
    print(f"[bold green]🔧 Generating code for prompt:[/bold green] '{prompt}'")
    generate_code(prompt)


@app.command()
def debug(path: str = typer.Argument(..., help="Path to the Python code or project directory.")):
    """Debug and lint code files."""
    print(f"[bold green]🛠️ Debugging code at:[/bold green] {path}")
    debug_code(path)


@app.command()
def uigen(theme: str = "light", components: str = "form"):
    """Generate UI components using templates."""
    print(f"[bold green]🎨 Generating UI with theme:[/bold green] {theme}, components: {components}")
    generate_ui(theme, components)


@app.command()
def validate(file: str, ci: bool = False):
    """Validate schema files or run full CI pipeline."""
    validate_file(file, ci)


@app.command()
def translate(from_lang: str, to_lang: str, filepath: str):
    """Translate code between programming languages."""
    print(f"[bold green]🔄 Translating {filepath} from {from_lang} to {to_lang}...[/bold green]")
    translate(from_lang, to_lang, filepath)


@app.command()
def mentor(question: str):
    """Ask logic or debugging questions to the mentor AI."""
    print(f"[bold green]❓ Asking mentor:[/bold green] {question}")
    mentor(question)


@app.command()
def visualize(prompt: str):
    """Generate an image or diagram from prompt."""
    print(f"[bold green]🖼️ Visualizing:[/bold green] {prompt}")
    visualize(prompt)


@app.command()
def deploy(target: str = "local"):
    """Deploy the current app to a target environment."""
    print(f"[bold green]🚀 Deploying to:[/bold green] {target}")
    deploy_cmd(target)


if __name__ == "__main__":
    app()