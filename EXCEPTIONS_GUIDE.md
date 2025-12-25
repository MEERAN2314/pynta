# Unifyt Exception Handling Guide

## 📋 Table of Contents

1. [Overview](#overview)
2. [Exception Hierarchy](#exception-hierarchy)
3. [Common Exceptions](#common-exceptions)
4. [Exception Categories](#exception-categories)
5. [Best Practices](#best-practices)
6. [Error Handling Patterns](#error-handling-patterns)
7. [Debugging Tips](#debugging-tips)
8. [Complete Reference](#complete-reference)

## Overview

Unifyt provides a comprehensive exception system with **25+ exception types** organized in a clear hierarchy. This allows you to catch specific errors or broad categories of errors as needed.

### Why Good Exception Handling?

✅ **Precise Error Catching**: Catch exactly the error you expect  
✅ **Clear Error Messages**: Understand what went wrong immediately  
✅ **Better Debugging**: Find and fix issues faster  
✅ **Robust Code**: Handle errors gracefully  
✅ **User-Friendly**: Provide helpful feedback  

## Exception Hierarchy

```
UnifytException (base)
├── UnitError
│   ├── DimensionalityError
│   ├── UnitNotFoundError
│   ├── UnitParseError
│   └── ConversionError
├── QuantityError
│   ├── InvalidValueError
│   ├── OperationError
│   ├── ComparisonError
│   ├── ArrayError
│   └── QuantityOverflowError
├── RegistryError
│   ├── UnitDefinitionError
│   ├── UnitAlreadyExistsError
│   └── UnitSystemError
├── SerializationError
│   ├── SerializationFormatError
│   ├── DeserializationError
│   └── SerializationVersionError
├── ContextError
│   ├── InvalidUnitSystemError
│   └── ContextStateError
├── ConstantError
├── UtilityError
├── ValidationError
├── PrecisionError
└── ConfigurationError
```

## Common Exceptions

### 1. DimensionalityError

**When**: Trying to perform operations on incompatible units

```python
from unifyt import Quantity
from unifyt.exceptions import DimensionalityError

try:
    distance = Quantity(100, 'meter')
    time = Quantity(10, 'second')
    result = distance + time  # Can't add length and time!
except DimensionalityError as e:
    print(f"Error: {e}")
    # Error: Cannot perform addition with incompatible dimensions: 'meter' and 'second'
```

**Attributes:**
- `unit1`: First unit
- `unit2`: Second unit
- `operation`: Operation attempted

**How to Fix:**
- Check that units are compatible
- Use correct operation (e.g., division instead of addition)
- Convert to compatible units first

### 2. ConversionError

**When**: Trying to convert between incompatible units

```python
from unifyt import Quantity
from unifyt.exceptions import ConversionError

try:
    distance = Quantity(100, 'meter')
    result = distance.to('second')  # Can't convert length to time!
except ConversionError as e:
    print(f"Error: {e}")
    # Error: Cannot convert from 'meter' to 'second'. Units have incompatible dimensions.
```

**Attributes:**
- `from_unit`: Source unit
- `to_unit`: Target unit
- `reason`: Optional reason for failure

**How to Fix:**
- Check that units have same dimensionality
- Verify unit names are correct
- Use compatible target unit

### 3. UnitNotFoundError

**When**: Using an unrecognized unit name

```python
from unifyt import Quantity
from unifyt.exceptions import UnitNotFoundError

try:
    distance = Quantity(100, 'metrs')  # Typo!
except UnitNotFoundError as e:
    print(f"Error: {e}")
    # Error: Unit 'metrs' not recognized. Did you mean: meter, meters?
```

**Attributes:**
- `unit_name`: The unit that wasn't found
- `suggestions`: List of similar unit names

**How to Fix:**
- Check spelling
- Use suggested unit names
- Check [UNITS_CATALOG.md](UNITS_CATALOG.md) for available units

### 4. InvalidValueError

**When**: Quantity value is invalid (NaN, infinity, etc.)

```python
from unifyt import Quantity
from unifyt.exceptions import InvalidValueError
import numpy as np

try:
    distance = Quantity(np.nan, 'meter')
    # Some operations may raise this
except InvalidValueError as e:
    print(f"Error: {e}")
```

**Attributes:**
- `value`: The invalid value
- `reason`: Why it's invalid
- `constraint`: Constraint that was violated

**How to Fix:**
- Validate input data
- Handle NaN/infinity before creating quantities
- Check data sources

### 5. OperationError

**When**: Operation cannot be performed

```python
from unifyt import Quantity
from unifyt.exceptions import OperationError

try:
    distance = Quantity(100, 'meter')
    result = distance + 50  # Can't add scalar to dimensioned quantity
except OperationError as e:
    print(f"Error: {e}")
```

**Attributes:**
- `operation`: The operation attempted
- `operand1`: First operand
- `operand2`: Second operand
- `reason`: Why it failed

**How to Fix:**
- Use compatible operands
- Create Quantity for scalar values
- Check operation is valid for types

## Exception Categories

### Unit Errors

Handle all unit-related errors:

```python
from unifyt import Quantity
from unifyt.exceptions import UnitError

try:
    # Any unit-related operation
    distance = Quantity(100, 'meter')
    result = distance.to('second')
except UnitError as e:
    print(f"Unit error: {e}")
```

**Catches:**
- DimensionalityError
- UnitNotFoundError
- UnitParseError
- ConversionError

### Quantity Errors

Handle all quantity-related errors:

```python
from unifyt import Quantity
from unifyt.exceptions import QuantityError

try:
    # Any quantity operation
    q1 = Quantity(100, 'meter')
    q2 = Quantity(10, 'second')
    result = q1 + q2
except QuantityError as e:
    print(f"Quantity error: {e}")
```

**Catches:**
- InvalidValueError
- OperationError
- ComparisonError
- ArrayError
- QuantityOverflowError

### Registry Errors

Handle custom unit definition errors:

```python
from unifyt import UnitRegistry
from unifyt.exceptions import RegistryError

try:
    registry = UnitRegistry()
    registry.define('bad_unit', 'invalid syntax')
except RegistryError as e:
    print(f"Registry error: {e}")
```

**Catches:**
- UnitDefinitionError
- UnitAlreadyExistsError
- UnitSystemError

### Serialization Errors

Handle save/load errors:

```python
from unifyt.serialization import load_quantity
from unifyt.exceptions import SerializationError

try:
    quantity = load_quantity('corrupted.json')
except SerializationError as e:
    print(f"Serialization error: {e}")
```

**Catches:**
- SerializationFormatError
- DeserializationError
- SerializationVersionError

## Best Practices

### 1. Catch Specific Exceptions

✅ **Good**: Catch specific exceptions
```python
from unifyt import Quantity
from unifyt.exceptions import ConversionError

try:
    result = distance.to('second')
except ConversionError:
    # Handle conversion error specifically
    print("Cannot convert between these units")
```

❌ **Bad**: Catch all exceptions
```python
try:
    result = distance.to('second')
except Exception:
    # Too broad - might hide other errors
    print("Something went wrong")
```

### 2. Use Exception Hierarchy

✅ **Good**: Catch category when appropriate
```python
from unifyt.exceptions import UnitError

try:
    # Multiple unit operations
    result = complex_calculation()
except UnitError:
    # Handles all unit-related errors
    print("Unit error occurred")
```

### 3. Provide Helpful Messages

✅ **Good**: Informative error handling
```python
from unifyt.exceptions import DimensionalityError

try:
    result = distance + time
except DimensionalityError as e:
    print(f"Cannot add {e.unit1} and {e.unit2}")
    print("Hint: Check that units are compatible")
```

### 4. Log Errors Appropriately

✅ **Good**: Log with context
```python
import logging
from unifyt.exceptions import UnifytException

logger = logging.getLogger(__name__)

try:
    result = calculation()
except UnifytException as e:
    logger.error(f"Unifyt error in calculation: {e}", exc_info=True)
    raise
```

### 5. Use Error Context

✅ **Good**: Add context to errors
```python
from unifyt.exceptions import ErrorContext

with ErrorContext("calculating velocity"):
    velocity = distance / time
    # Any errors will include context
```

## Error Handling Patterns

### Pattern 1: Validation

```python
from unifyt import Quantity
from unifyt.exceptions import InvalidValueError, UnitNotFoundError

def create_distance(value, unit):
    """Create distance quantity with validation."""
    try:
        distance = Quantity(value, unit)
        
        # Validate value
        if distance.magnitude < 0:
            raise InvalidValueError(
                value, 
                "Distance cannot be negative",
                "must be non-negative"
            )
        
        return distance
        
    except UnitNotFoundError as e:
        print(f"Invalid unit: {e.unit_name}")
        if e.suggestions:
            print(f"Did you mean: {', '.join(e.suggestions)}?")
        raise
```

### Pattern 2: Graceful Degradation

```python
from unifyt import Quantity
from unifyt.exceptions import ConversionError

def convert_with_fallback(quantity, target_unit, fallback_unit='meter'):
    """Try conversion, fall back to default unit."""
    try:
        return quantity.to(target_unit)
    except ConversionError:
        print(f"Cannot convert to {target_unit}, using {fallback_unit}")
        return quantity.to(fallback_unit)
```

### Pattern 3: Retry with Different Units

```python
from unifyt import Quantity
from unifyt.exceptions import UnitNotFoundError

def create_quantity_flexible(value, *unit_names):
    """Try creating quantity with multiple unit names."""
    for unit_name in unit_names:
        try:
            return Quantity(value, unit_name)
        except UnitNotFoundError:
            continue
    
    raise UnitNotFoundError(
        unit_names[0],
        list(unit_names[1:])
    )

# Usage
distance = create_quantity_flexible(100, 'meters', 'meter', 'm')
```

### Pattern 4: Batch Processing with Error Collection

```python
from unifyt import Quantity
from unifyt.exceptions import UnifytException

def process_measurements(data):
    """Process measurements, collecting errors."""
    results = []
    errors = []
    
    for item in data:
        try:
            quantity = Quantity(item['value'], item['unit'])
            converted = quantity.to('meter')
            results.append(converted)
        except UnifytException as e:
            errors.append({
                'item': item,
                'error': str(e)
            })
    
    return results, errors
```

### Pattern 5: Custom Error Messages

```python
from unifyt import Quantity
from unifyt.exceptions import DimensionalityError

def calculate_speed(distance, time):
    """Calculate speed with helpful error messages."""
    try:
        return distance / time
    except DimensionalityError as e:
        raise ValueError(
            f"Cannot calculate speed: distance has unit {e.unit1}, "
            f"time has unit {e.unit2}. "
            f"Ensure distance is a length and time is a duration."
        ) from e
```

## Debugging Tips

### 1. Check Exception Attributes

```python
from unifyt.exceptions import ConversionError

try:
    result = distance.to('second')
except ConversionError as e:
    print(f"From: {e.from_unit}")
    print(f"To: {e.to_unit}")
    print(f"Reason: {e.reason}")
```

### 2. Use repr() for Details

```python
from unifyt.exceptions import UnifytException

try:
    result = operation()
except UnifytException as e:
    print(repr(e))  # Shows exception class and message
```

### 3. Enable Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('unifyt')

# Now Unifyt operations will log details
```

### 4. Use Error Context

```python
from unifyt.exceptions import ErrorContext

with ErrorContext("processing sensor data"):
    with ErrorContext("converting units"):
        result = quantity.to('meter')
        # Errors will show: "... (context: converting units)"
```

### 5. Check Stack Trace

```python
import traceback
from unifyt.exceptions import UnifytException

try:
    result = operation()
except UnifytException as e:
    traceback.print_exc()  # Shows full stack trace
```

## Complete Reference

### All Exception Types

#### Base Exception
- **UnifytException**: Base for all Unifyt exceptions

#### Unit Errors
- **UnitError**: Base for unit errors
- **DimensionalityError**: Incompatible dimensions
- **UnitNotFoundError**: Unit not recognized
- **UnitParseError**: Cannot parse unit string
- **ConversionError**: Cannot convert units

#### Quantity Errors
- **QuantityError**: Base for quantity errors
- **InvalidValueError**: Invalid quantity value
- **OperationError**: Invalid operation
- **ComparisonError**: Cannot compare quantities
- **ArrayError**: Array operation failed
- **QuantityOverflowError**: Overflow in calculation

#### Registry Errors
- **RegistryError**: Base for registry errors
- **UnitDefinitionError**: Invalid unit definition
- **UnitAlreadyExistsError**: Unit already defined
- **UnitSystemError**: Unit system error

#### Serialization Errors
- **SerializationError**: Base for serialization errors
- **SerializationFormatError**: Unsupported format
- **DeserializationError**: Cannot deserialize
- **SerializationVersionError**: Version incompatible

#### Context Errors
- **ContextError**: Base for context errors
- **InvalidUnitSystemError**: Invalid unit system
- **ContextStateError**: Invalid context state

#### Other Errors
- **ConstantError**: Constant not found
- **UtilityError**: Utility function failed
- **ValidationError**: Validation failed
- **PrecisionError**: Precision loss
- **ConfigurationError**: Invalid configuration

### Exception Utilities

#### ErrorContext

```python
from unifyt.exceptions import ErrorContext

with ErrorContext("description"):
    # Code that might raise exceptions
    pass
```

#### create_exception

```python
from unifyt.exceptions import create_exception, UnitError

exc = create_exception(
    UnitError,
    "Custom error message",
    custom_attr="value"
)
```

## Examples

### Example 1: Robust Unit Conversion

```python
from unifyt import Quantity
from unifyt.exceptions import ConversionError, UnitNotFoundError

def safe_convert(value, from_unit, to_unit):
    """Safely convert with error handling."""
    try:
        quantity = Quantity(value, from_unit)
        return quantity.to(to_unit)
    except UnitNotFoundError as e:
        print(f"Unknown unit: {e.unit_name}")
        if e.suggestions:
            print(f"Suggestions: {', '.join(e.suggestions)}")
        return None
    except ConversionError as e:
        print(f"Cannot convert {e.from_unit} to {e.to_unit}")
        return None

# Usage
result = safe_convert(100, 'meter', 'kilometer')
if result:
    print(f"Result: {result}")
```

### Example 2: Batch Processing

```python
from unifyt import Quantity
from unifyt.exceptions import UnifytException

def process_batch(measurements):
    """Process batch with error handling."""
    successful = []
    failed = []
    
    for i, (value, unit) in enumerate(measurements):
        try:
            q = Quantity(value, unit)
            q_si = q.to_base_units()
            successful.append((i, q_si))
        except UnifytException as e:
            failed.append((i, str(e)))
    
    return successful, failed

# Usage
measurements = [
    (100, 'meter'),
    (50, 'invalid_unit'),
    (200, 'kilometer')
]

good, bad = process_batch(measurements)
print(f"Processed: {len(good)}, Failed: {len(bad)}")
```

### Example 3: User Input Validation

```python
from unifyt import Quantity
from unifyt.exceptions import UnitNotFoundError, InvalidValueError

def get_distance_from_user():
    """Get distance from user with validation."""
    while True:
        try:
            value = float(input("Enter distance value: "))
            unit = input("Enter unit (e.g., meter, km, mile): ")
            
            distance = Quantity(value, unit)
            
            if distance.magnitude < 0:
                print("Distance must be positive!")
                continue
            
            return distance
            
        except ValueError:
            print("Invalid number!")
        except UnitNotFoundError as e:
            print(f"Unknown unit: {e.unit_name}")
            if e.suggestions:
                print(f"Did you mean: {', '.join(e.suggestions)}?")
        except InvalidValueError as e:
            print(f"Invalid value: {e.reason}")
```

## Summary

### Key Takeaways

1. **Use Specific Exceptions**: Catch exactly what you expect
2. **Leverage Hierarchy**: Catch categories when appropriate
3. **Provide Context**: Help users understand errors
4. **Handle Gracefully**: Don't let errors crash your program
5. **Log Appropriately**: Record errors for debugging

### Quick Reference

```python
# Catch specific error
from unifyt.exceptions import ConversionError
try:
    result = quantity.to('meter')
except ConversionError:
    # Handle conversion error
    pass

# Catch category
from unifyt.exceptions import UnitError
try:
    result = operation()
except UnitError:
    # Handle any unit error
    pass

# Catch all Unifyt errors
from unifyt.exceptions import UnifytException
try:
    result = operation()
except UnifytException:
    # Handle any Unifyt error
    pass

# Add context
from unifyt.exceptions import ErrorContext
with ErrorContext("operation name"):
    result = operation()
```

---

**For more information:**
- [API Reference](docs/api_reference.md)
- [User Guide](docs/user_guide.md)
- [Examples](examples/)

**Unifyt** - Making unit conversions simple, safe, and powerful! 🚀
