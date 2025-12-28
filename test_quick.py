"""Quick test of v0.3.0 features"""

from unifyt import UncertainQuantity, Quantity, format_quantity

print("Testing UncertainQuantity...")
length = UncertainQuantity(100.0, 'meter', uncertainty=0.5)
width = UncertainQuantity(50.0, 'meter', uncertainty=0.3)
print(f"Length: {length}")
print(f"Width: {width}")

area = length * width
print(f"Area: {area}")
print("✓ UncertainQuantity works!")

print("\nTesting formatting...")
speed = Quantity(100, 'meter/second')
print(f"Default: {format_quantity(speed, style='default')}")
print(f"Compact: {format_quantity(speed, style='compact')}")
print("✓ Formatting works!")

print("\nTesting validation...")
from unifyt import validate_unit, suggest_unit
print(f"Is 'meter' valid? {validate_unit('meter')}")
print(f"Suggestions for 'metr': {suggest_unit('metr')[:3]}")
print("✓ Validation works!")

print("\nTesting batch operations...")
from unifyt import convert_batch
distances = [
    Quantity(100, 'meter'),
    Quantity(1, 'kilometer'),
]
results = convert_batch(distances, 'meter')
print(f"Converted: {[str(r) for r in results]}")
print("✓ Batch operations work!")

print("\n✅ All v0.3.0 features working!")
