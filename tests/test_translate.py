from src.translate import XLangTranslator
import os

def test_translation_creates_output():
    with open("sample.js", "w") as f:
        f.write("console.log('Hello');")
    translator = XLangTranslator("js", "py")
    translator.translate_file("sample.js", output_dir="translated")
    assert os.path.exists("translated/translated_sample.py")
