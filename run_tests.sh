#!/bin/bash
# Script to run tests for Pynta library

echo "=== Running Pynta Tests ==="
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "pytest not found. Installing dependencies..."
    pip install -e ".[dev]"
fi

# Run tests with coverage
echo "Running tests with coverage..."
pytest tests/ -v --cov=pynta --cov-report=term --cov-report=html

echo ""
echo "=== Test Results ==="
echo "Coverage report generated in htmlcov/index.html"
