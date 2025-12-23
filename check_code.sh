#!/bin/bash
# Script to check code quality

echo "=== Running Code Quality Checks ==="
echo ""

# Check if tools are installed
if ! command -v black &> /dev/null; then
    echo "Installing code quality tools..."
    pip install black flake8 mypy isort
fi

echo "--- Running Black (formatter) ---"
black --check pynta/ tests/ examples/
echo ""

echo "--- Running isort (import sorter) ---"
isort --check-only pynta/ tests/ examples/
echo ""

echo "--- Running Flake8 (linter) ---"
flake8 pynta/ --max-line-length=100 --extend-ignore=E203,W503
echo ""

echo "--- Running MyPy (type checker) ---"
mypy pynta/ --ignore-missing-imports
echo ""

echo "=== Code Quality Check Complete ==="
