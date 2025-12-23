#!/bin/bash
# Script to run all example files

echo "=== Running Pynta Examples ==="
echo ""

# Check if pynta is installed
if ! python -c "import pynta" 2>/dev/null; then
    echo "Pynta not found. Installing..."
    pip install -e .
fi

echo "--- Basic Usage ---"
python examples/basic_usage.py
echo ""

echo "--- Scientific Calculations ---"
python examples/scientific_calculations.py
echo ""

echo "--- Custom Units ---"
python examples/custom_units.py
echo ""

echo "--- Array Operations ---"
python examples/array_operations.py
echo ""

echo "--- Advanced Features ---"
python examples/advanced_features.py
echo ""

echo "--- Complete Demo ---"
python examples/complete_demo.py
echo ""

echo "=== All Examples Completed ==="
