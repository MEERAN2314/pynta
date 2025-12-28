"""Examples showcasing new features in Unifyt v0.3.0"""

from unifyt import (
    Quantity,
    UncertainQuantity,
    QuantityFormatter,
    format_quantity,
    UnitValidator,
    validate_unit,
    suggest_unit,
    BatchConverter,
    convert_batch,
    sum_batch,
    get_profiler,
    enable_profiling,
    print_profiling_stats,
    UnitRegistry,
    prefixes
)
import numpy as np

print("=" * 70)
print("UNIFYT v0.3.0 - NEW FEATURES SHOWCASE")
print("=" * 70)

# ============================================================================
# 1. UNCERTAIN QUANTITIES - Measurements with error margins
# ============================================================================
print("\n" + "=" * 70)
print("1. UNCERTAIN QUANTITIES - Error Propagation")
print("=" * 70)

# Create measurements with uncertainties
length = UncertainQuantity(100.0, 'meter', uncertainty=0.5)
width = UncertainQuantity(50.0, 'meter', uncertainty=0.3)

print(f"\nLength: {length}")
print(f"Width: {width}")

# Automatic error propagation in calculations
area = length * width
print(f"\nArea: {area}")
print(f"Relative uncertainty: {area.relative_uncertainty.item():.4f}")

# More complex calculations
height = UncertainQuantity(10.0, 'meter', uncertainty=0.1)
volume = area * height
print(f"\nVolume: {volume}")

# Convert with uncertainty preserved
volume_liters = volume.to('liter')
print(f"Volume in liters: {volume_liters}")

# ============================================================================
# 2. ADVANCED FORMATTING - Multiple output styles
# ============================================================================
print("\n" + "=" * 70)
print("2. ADVANCED FORMATTING")
print("=" * 70)

speed = Quantity(100, 'meter/second')

print(f"\nOriginal: {speed}")
print(f"LaTeX: {format_quantity(speed, style='latex')}")
print(f"Unicode: {format_quantity(speed, style='unicode')}")
print(f"HTML: {format_quantity(speed, style='html')}")
print(f"Compact: {format_quantity(speed, style='compact')}")
print(f"Scientific: {format_quantity(speed, style='scientific')}")

# Custom formatter
formatter = QuantityFormatter(style='latex', precision=3)
energy = Quantity(1.602e-19, 'joule')
print(f"\nEnergy (LaTeX, 3 digits): {formatter.format(energy)}")

# ============================================================================
# 3. UNIT VALIDATION - Check units before use
# ============================================================================
print("\n" + "=" * 70)
print("3. UNIT VALIDATION")
print("=" * 70)

validator = UnitValidator()

# Validate units
print(f"\nIs 'meter' valid? {validate_unit('meter')}")
print(f"Is 'invalid_unit' valid? {validate_unit('invalid_unit')}")

# Get suggestions for typos
print(f"\nSuggestions for 'metr': {suggest_unit('metr')}")
print(f"Suggestions for 'secnd': {suggest_unit('secnd')}")

# Check dimensionality compatibility
is_compat, msg = validator.check_dimensionality('meter', 'foot')
print(f"\nAre 'meter' and 'foot' compatible? {is_compat}")

is_compat, msg = validator.check_dimensionality('meter', 'second')
print(f"Are 'meter' and 'second' compatible? {is_compat}")
if msg:
    print(f"  Reason: {msg}")

# Simplify complex units
complex_unit = 'meter * second / second'
simplified = validator.simplify_unit(complex_unit)
print(f"\nSimplified '{complex_unit}' -> '{simplified}'")

# ============================================================================
# 4. BATCH OPERATIONS - Process multiple quantities efficiently
# ============================================================================
print("\n" + "=" * 70)
print("4. BATCH OPERATIONS")
print("=" * 70)

# Create multiple quantities
distances = [
    Quantity(100, 'meter'),
    Quantity(1, 'kilometer'),
    Quantity(50, 'foot'),
    Quantity(1, 'mile')
]

print("\nOriginal distances:")
for d in distances:
    print(f"  {d}")

# Convert all to same unit
converter = BatchConverter()
distances_km = converter.convert_all(distances, 'kilometer')

print("\nAll converted to kilometers:")
for d in distances_km:
    print(f"  {d}")

# Calculate statistics
total = converter.sum_quantities(distances)
mean = converter.mean_quantities(distances)
min_dist = converter.min_quantity(distances)
max_dist = converter.max_quantity(distances)

print(f"\nStatistics:")
print(f"  Total: {total.to('kilometer')}")
print(f"  Mean: {mean.to('kilometer')}")
print(f"  Min: {min_dist.to('meter')}")
print(f"  Max: {max_dist.to('kilometer')}")

# Quick batch functions
quick_converted = convert_batch(distances, 'meter')
quick_sum = sum_batch(distances)
print(f"\nQuick sum: {quick_sum.to('kilometer')}")

# ============================================================================
# 5. PERFORMANCE PROFILING - Monitor operation performance
# ============================================================================
print("\n" + "=" * 70)
print("5. PERFORMANCE PROFILING")
print("=" * 70)

enable_profiling()
profiler = get_profiler()

# Profile conversions
print("\nProfiling 1000 unit conversions...")
with profiler.profile('conversion'):
    for _ in range(1000):
        q = Quantity(100, 'meter').to('kilometer')

# Profile arithmetic
print("Profiling 1000 arithmetic operations...")
with profiler.profile('arithmetic'):
    for _ in range(1000):
        a = Quantity(100, 'meter')
        b = Quantity(50, 'second')
        c = a / b

# Profile array operations
print("Profiling 100 array operations...")
with profiler.profile('array_ops'):
    for _ in range(100):
        arr = Quantity(np.random.rand(1000), 'meter')
        result = arr.to('kilometer')

# Print statistics
print_profiling_stats()

# ============================================================================
# 6. METRIC PREFIXES - Auto-generate prefixed units
# ============================================================================
print("\n" + "=" * 70)
print("6. METRIC PREFIXES")
print("=" * 70)

# Create registry with prefixes
registry = UnitRegistry()

# Add prefixes to a custom unit
registry.define('parsec', '3.086e16 meter')
prefixes.add_prefixes_to_unit(
    registry,
    'parsec',
    '3.086e16 meter',
    prefixes=['kilo', 'mega', 'giga']
)

print("\nGenerated prefixed units for 'parsec':")
print("  kiloparsec, megaparsec, gigaparsec")

# Generate common prefixed units
prefixes.generate_common_prefixed_units(registry)
print("\nGenerated common prefixed units:")
print("  kilometer, centimeter, millimeter, etc.")

# Parse prefixed units
base, factor = prefixes.parse_prefixed_unit('kilometer')
print(f"\nParsed 'kilometer': base='{base}', factor={factor}")

# ============================================================================
# 7. REAL-WORLD EXAMPLE - Experimental Physics
# ============================================================================
print("\n" + "=" * 70)
print("7. REAL-WORLD EXAMPLE - Experimental Physics Measurement")
print("=" * 70)

# Measure pendulum period with uncertainty
period = UncertainQuantity(2.01, 'second', uncertainty=0.02)
length = UncertainQuantity(1.00, 'meter', uncertainty=0.01)

print(f"\nPendulum measurements:")
print(f"  Period: {period}")
print(f"  Length: {length}")

# Calculate gravitational acceleration: g = 4π²L/T²
import math
pi_squared = math.pi ** 2
g = (4 * pi_squared * length) / (period ** 2)

print(f"\nCalculated g: {g}")
print(f"Relative uncertainty: {g.relative_uncertainty.item():.4%}")

# Compare with known value
g_known = Quantity(9.81, 'meter/second^2')
difference = abs(g.value.item() - g_known.value.item())
print(f"\nKnown g: {g_known}")
print(f"Difference: {difference:.3f} m/s²")
print(f"Within uncertainty? {difference < g.uncertainty.item()}")

# ============================================================================
# 8. BATCH ANALYSIS - Multiple Experiments
# ============================================================================
print("\n" + "=" * 70)
print("8. BATCH ANALYSIS - Multiple Experiments")
print("=" * 70)

# Multiple measurements from different experiments
measurements = [
    UncertainQuantity(9.78, 'meter/second^2', uncertainty=0.05),
    UncertainQuantity(9.82, 'meter/second^2', uncertainty=0.04),
    UncertainQuantity(9.80, 'meter/second^2', uncertainty=0.06),
    UncertainQuantity(9.81, 'meter/second^2', uncertainty=0.03),
]

print("\nExperimental measurements of g:")
for i, m in enumerate(measurements, 1):
    print(f"  Experiment {i}: {m}")

# Calculate mean
mean_g = converter.mean_quantities(measurements)
print(f"\nMean value: {mean_g}")

# Find best measurement (smallest uncertainty)
uncertainties = [m.uncertainty.item() for m in measurements]
best_idx = np.argmin(uncertainties)
print(f"Most precise measurement: Experiment {best_idx + 1}")

print("\n" + "=" * 70)
print("END OF v0.3.0 FEATURES SHOWCASE")
print("=" * 70)
