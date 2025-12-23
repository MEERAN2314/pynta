#!/bin/bash
# Script to format code automatically

echo "=== Formatting Code ==="
echo ""

# Check if tools are installed
if ! command -v black &> /dev/null; then
    echo "Installing formatting tools..."
    pip install black isort
fi

echo "--- Running Black ---"
black pynta/ tests/ examples/
echo ""

echo "--- Running isort ---"
isort pynta/ tests/ examples/
echo ""

echo "=== Code Formatting Complete ==="
