from pathlib import Path
from typing import List
from rich import print
import random
import datetime

# === Component Library ===
UI_COMPONENTS = {
    "hero": lambda theme: f"""
<section class='bg-{theme}-900 text-white p-12'>
  <div class='max-w-7xl mx-auto'>
    <h1 class='text-5xl font-bold mb-4'>Welcome to Qwnt AI</h1>
    <p class='text-lg'>Empowering developers with quantum-enhanced intelligence.</p>
    <a href="#" class='mt-6 inline-block px-6 py-3 bg-{theme}-600 text-white font-medium rounded shadow hover:bg-{theme}-700'>Get Started</a>
  </div>
</section>
""",

    "features": lambda theme: f"""
<section class='bg-{theme}-50 text-gray-800 py-12'>
  <div class='max-w-6xl mx-auto px-6'>
    <h2 class='text-3xl font-semibold mb-8'>Platform Capabilities</h2>
    <div class='grid grid-cols-1 md:grid-cols-3 gap-6'>
      <div class='p-6 border rounded shadow'>
        <h3 class='text-xl font-bold'>Code Generation</h3>
        <p>Write structured applications from natural prompts.</p>
      </div>
      <div class='p-6 border rounded shadow'>
        <h3 class='text-xl font-bold'>Quantum Debugging</h3>
        <p>Catch bugs using entropy-guided fault detection.</p>
      </div>
      <div class='p-6 border rounded shadow'>
        <h3 class='text-xl font-bold'>Visual Interfaces</h3>
        <p>Drag-and-drop builder with dark/light themes.</p>
      </div>
    </div>
  </div>
</section>
""",

    "pricing": lambda theme: f"""
<section class='bg-{theme}-100 text-gray-900 py-16'>
  <div class='max-w-4xl mx-auto px-4'>
    <h2 class='text-3xl font-bold mb-6'>Pricing Plans</h2>
    <div class='grid grid-cols-1 md:grid-cols-3 gap-8'>
      <div class='bg-white p-6 rounded shadow'>
        <h3 class='text-xl font-semibold'>Free</h3>
        <p class='text-sm mt-2'>Basic tooling access</p>
        <p class='text-2xl mt-4 font-bold'>$0</p>
      </div>
      <div class='bg-white p-6 rounded shadow border border-{theme}-500'>
        <h3 class='text-xl font-semibold text-{theme}-700'>Pro</h3>
        <p class='text-sm mt-2'>Full API + Qwnt SDK</p>
        <p class='text-2xl mt-4 font-bold'>$29/month</p>
      </div>
      <div class='bg-white p-6 rounded shadow'>
        <h3 class='text-xl font-semibold'>Enterprise</h3>
        <p class='text-sm mt-2'>Custom on-premise deployments</p>
        <p class='text-2xl mt-4 font-bold'>Contact Us</p>
      </div>
    </div>
  </div>
</section>
""",

    "footer": lambda theme: f"""
<footer class='bg-{theme}-800 text-white py-6'>
  <div class='max-w-7xl mx-auto px-6 flex justify-between'>
    <p>&copy; {datetime.datetime.now().year} Qwnt AI. All rights reserved.</p>
    <div class='space-x-4'>
      <a href='#' class='hover:underline'>Docs</a>
      <a href='#' class='hover:underline'>API</a>
      <a href='#' class='hover:underline'>Support</a>
    </div>
  </div>
</footer>
"""
}

# === UI Generator ===
def generate_ui(theme: str = "slate", components: List[str] = ["hero", "features", "pricing", "footer"], output_dir: str = "quill_ui"):
    print(f"[bold magenta]🎨 Generating multi-section website with theme:[/bold magenta] {theme}")
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    selected_components = [comp for comp in components if comp in UI_COMPONENTS]
    random.shuffle(selected_components)  # Simulate creative permutation

    html_blocks = [UI_COMPONENTS[comp](theme) for comp in selected_components]

    html_doc = f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Qwnt AI Site</title>
  <script src=\"https://cdn.tailwindcss.com\"></script>
</head>
<body class='antialiased'>
{''.join(html_blocks)}
</body>
</html>
"""

    file_path = output_path / "index.html"
    file_path.write_text(html_doc)

    print(f"[green]✔ Full website generated at:[/green] {file_path.resolve()}")
    print("[bold green]\n✅ Done. Ready to serve as a landing page or app frontend.[/bold green]")