from src.codegen import generate_code
import os

def test_generate_code_creates_output():
    prompt = "Build a basic Flask API"
    output_dir = "test_output"
    generate_code(prompt, output_dir=output_dir)
    assert os.path.exists(f"{output_dir}/main.py")
