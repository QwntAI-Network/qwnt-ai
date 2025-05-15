.PHONY: help install test lint type-check format run dev deploy clean

help:
	@echo "Usage:"
	@echo "  make install      Install all dependencies"
	@echo "  make test         Run all unit tests"
	@echo "  make lint         Run flake8 for linting"
	@echo "  make type-check   Run mypy for static type checks"
	@echo "  make format       Run black for code formatting"
	@echo "  make run          Launch CLI help"
	@echo "  make deploy       Deploy locally (default)"
	@echo "  make clean        Remove output/test/generated files"

install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 src/ tests/

type-check:
	mypy src/

format:
	black src/ tests/

run:
	python -m src.main --help

deploy:
	python -m src.main deploy

clean:
	rm -rf test_output quill_output quill_visuals translated __pycache__ .mypy_cache .pytest_cache
