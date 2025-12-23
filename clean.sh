#!/bin/bash
# Clean up temporary and generated files

echo "=== Cleaning Pynta Project ==="
echo ""

# Remove Python cache files
echo "Removing Python cache files..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
find . -type f -name "*.pyo" -delete 2>/dev/null
find . -type f -name "*.pyd" -delete 2>/dev/null

# Remove pytest cache
echo "Removing pytest cache..."
rm -rf .pytest_cache 2>/dev/null
rm -rf .coverage 2>/dev/null
rm -rf htmlcov 2>/dev/null

# Remove build artifacts
echo "Removing build artifacts..."
rm -rf build 2>/dev/null
rm -rf dist 2>/dev/null
rm -rf *.egg-info 2>/dev/null
rm -rf .eggs 2>/dev/null

# Remove mypy cache
echo "Removing mypy cache..."
rm -rf .mypy_cache 2>/dev/null

# Remove temporary files
echo "Removing temporary files..."
find . -type f -name "*~" -delete 2>/dev/null
find . -type f -name "*.swp" -delete 2>/dev/null
find . -type f -name "*.swo" -delete 2>/dev/null
find . -type f -name ".DS_Store" -delete 2>/dev/null

echo ""
echo "=== Cleanup Complete ==="
echo "Project is now clean!"
