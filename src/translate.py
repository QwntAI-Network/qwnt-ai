from pathlib import Path
from rich import print
from typing import Optional
import difflib
import os

# === Supported Language Mapping (Canonicalized) ===
LANGUAGE_MAP = {
    "py": "python",
    "js": "javascript",
    "ts": "typescript",
    "c": "c",
    "cpp": "cpp",
    "java": "java",
    "cs": "csharp",
    "go": "golang",
    "rb": "ruby",
    "php": "php",
    "rs": "rust",
    "kt": "kotlin",
    "swift": "swift",
    "scala": "scala",
    "sol": "solidity",
    "html": "html",
    "css": "css",
    "json": "json",
    "xml": "xml",
    "sh": "bash",
    "sql": "sql",
    "r": "r",
    "lua": "lua",
    "perl": "perl",
    "dart": "dart",
    "elixir": "elixir",
    "haskell": "haskell",
    "clj": "clojure",
    "jl": "julia",
    "md": "markdown",
    "yaml": "yaml",
    "toml": "toml",
    "ini": "ini",
    "bat": "batch",
    "pl": "prolog",
    "f90": "fortran",
    "asm": "assembly",
    "tex": "latex",
    "groovy": "groovy",
    "vue": "vue",
    "svelte": "svelte",
    "tsx": "tsx",
    "jsx": "jsx",
    "erl": "erlang",
    "nim": "nim",
    "zig": "zig",
    "vala": "vala",
    "nimrod": "nimrod",
    "tcl": "tcl",
    "coffeescript": "coffeescript",
    "ocaml": "ocaml",
    "vb": "vbnet",
    "abap": "abap",
    "ada": "ada",
    "awk": "awk",
    "powershell": "powershell",
    "cr": "crystal",
    "d": "d",
    "rexx": "rexx"
}

# === Translator Engine ===
class XLangTranslator:
    def __init__(self, source_lang: str, target_lang: str):
        self.source = LANGUAGE_MAP.get(source_lang, source_lang)
        self.target = LANGUAGE_MAP.get(target_lang, target_lang)

    def translate_file(self, input_path: str, output_dir: Optional[str] = None):
        source_file = Path(input_path)
        if not source_file.exists():
            print(f"[red]✖ Source file not found: {input_path}[/red]")
            return

        code = source_file.read_text()
        translated_code = self._simulate_translation(code)

        output_path = Path(output_dir or "quill_translations")
        output_path.mkdir(parents=True, exist_ok=True)
        outfile = output_path / f"translated_{source_file.stem}.{self.target}"
        outfile.write_text(translated_code)

        print(f"[green]✔ Translated file saved:[/green] {outfile.resolve()}")
        print("[bold green]\n✅ Translation complete. You can now review or deploy the output.[/bold green]")

    def _simulate_translation(self, code: str) -> str:
        """
        Placeholder logic for now. Can be replaced with ML inference or rules engine.
        """
        banner = f"// Translation from {self.source} to {self.target} using Qwnt AI Engine\n"
        return banner + code


# === CLI Entry ===
def translate(from_lang: str, to_lang: str, filepath: str):
    print(f"[bold cyan]🔄 XLang-TX Translating from {from_lang} to {to_lang}...[/bold cyan]")
    engine = XLangTranslator(from_lang.lower(), to_lang.lower())
    engine.translate_file(filepath)