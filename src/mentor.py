from rich import print
import random
import textwrap

# === KN-Bridge / Mentor AI ===
class MentorAI:
    def __init__(self):
        self.curriculum = self._build_curriculum()

    def _build_curriculum(self):
        return {
            "python": [
                "[1] Beginner: Learn variables, types, loops, and conditionals.",
                "[2] Intermediate: Practice functions, modules, file I/O, and error handling.",
                "[3] Advanced: Master decorators, generators, OOP, and context managers.",
                "[4] Expert: Dive into concurrency (async/threading), memory profiling, metaclasses, and bytecode."
            ],
            "javascript": [
                "[1] Beginner: Understand syntax, variables, functions, and basic DOM.",
                "[2] Intermediate: Learn closures, ES6 features, promises, and fetch API.",
                "[3] Advanced: Explore prototypes, async/await, module systems.",
                "[4] Expert: Study event loop internals, performance tuning, and security patterns."
            ],
            "rust": [
                "[1] Beginner: Learn let-bindings, primitive types, and ownership rules.",
                "[2] Intermediate: Use structs, enums, pattern matching, and error handling.",
                "[3] Advanced: Implement traits, lifetimes, and concurrency models.",
                "[4] Expert: Explore unsafe Rust, macros, and compiler internals."
            ]
        }

    def ask(self, question: str, lang: str = "python", level: str = "beginner") -> str:
        lang = lang.lower()
        level = level.lower()

        print(f"[bold cyan]🧠 Mentor AI Activated[/bold cyan]\n")
        if lang not in self.curriculum:
            return f"Sorry, curriculum for [bold]{lang}[/bold] is not available yet."

        roadmap = self.curriculum[lang]
        level_index = {"beginner": 0, "intermediate": 1, "advanced": 2, "expert": 3}.get(level, 0)
        lesson = roadmap[level_index]

        explanation = self._explain_concept(question, lang, level_index)
        return f"{lesson}\n\n{explanation}"

    def _explain_concept(self, concept: str, lang: str, level_index: int) -> str:
        examples = {
            ("python", 0): "Variables in Python are dynamically typed. For example: x = 42",
            ("python", 1): "Functions are defined using 'def'. You can import modules using 'import os'",
            ("python", 2): "Generators allow lazy iteration. Example: def gen(): yield 1",
            ("python", 3): "Metaclasses are classes of classes. Used to customize class creation dynamically.",

            ("javascript", 0): "Use 'let' or 'const' for variable declarations. Example: let count = 5;",
            ("javascript", 1): "Closures capture surrounding scope. Example: function outer() { let x = 1; return function() { return x; }; }",
            ("javascript", 2): "Async/await lets you write promise-based code like synchronous code.",
            ("javascript", 3): "The event loop handles async tasks. Study microtask queue and task queue separation.",

            ("rust", 0): "Rust variables are immutable by default. Use 'mut' to make them mutable.",
            ("rust", 1): "Pattern matching with 'match' enables exhaustive condition handling.",
            ("rust", 2): "Lifetimes are annotations that tell the compiler how long references are valid.",
            ("rust", 3): "Unsafe Rust allows you to dereference raw pointers, useful for FFI or low-level ops."
        }
        return examples.get((lang, level_index), f"Here's a general explanation for '{concept}' in {lang}.")


# === CLI Entry ===
def mentor(question: str, lang: str = "python", level: str = "beginner"):
    mentor_bot = MentorAI()
    response = mentor_bot.ask(question, lang, level)
    print(f"[bold green]📘 Response:[/bold green]\n{textwrap.indent(response, '  ')}\n")
