# Universal Volume to Cubic Meter Converter

## Overview

This is a specialized example that demonstrates converting **any volume unit to cubic meters (m³)**. It's designed for practical use cases where volume measurements need to be standardized.

## Features

✅ **Interactive Mode** - Enter values and units interactively  
✅ **Command-Line Mode** - Quick conversions from terminal  
✅ **Batch Conversion** - Convert multiple volumes at once  
✅ **Demonstration Mode** - See common conversion examples  
✅ **Practical Applications** - Real-world scenarios  
✅ **Error Handling** - Graceful handling of invalid inputs  

## Usage

### 1. Interactive Mode

```bash
python volume_to_cubic_meter.py
```

Then enter values like:
```
Enter value and unit (e.g., '100 liter'): 100 liter
Enter value and unit (e.g., '100 liter'): 50 gallon
Enter value and unit (e.g., '100 liter'): help
Enter value and unit (e.g., '100 liter'): quit
```

### 2. Direct Conversion

```bash
# Convert 100 liters to cubic meters
python volume_to_cubic_meter.py 100 liter

# Convert 50 gallons to cubic meters
python volume_to_cubic_meter.py 50 gallon

# Convert 2.5 cubic meters (shows it's already in m³)
python volume_to_cubic_meter.py 2.5 cubic_meter
```

### 3. Demonstration Mode

```bash
# See common conversion examples
python volume_to_cubic_meter.py --demo
```

### 4. Practical Applications

```bash
# See real-world application scenarios
python volume_to_cubic_meter.py --apps
```

### 5. Help

```bash
# Show supported units and usage
python volume_to_cubic_meter.py --help
```

## Supported Units

### Metric
- `cubic_meter` (m³, m3, m^3)
- `liter` (L, liters, litre, litres)
- `milliliter` (mL, milliliters)

### Imperial/US
- `gallon` (gal, gallons)
- `quart` (qt)
- `pint` (pt)
- `cup` (cups)
- `fluid_ounce` (fl_oz)

## Example Outputs

### Direct Conversion
```
======================================================================
CONVERSION RESULT
======================================================================

Original:      100.0 liter
Cubic Meters:  0.1 cubic_meter
Liters:        100.0 liter

Numerical Values:
  m³:  0.100000
  L:   100.000000
======================================================================
```

### Batch Conversion
```
Description                    Original             Cubic Meters (m³)   
----------------------------------------------------------------------
Water tank                     1000 liter           1.000000            
Fuel tank                      50 gallon            0.189271            
Bottle                         500 milliliter       0.000500            
Room volume                    2.5 cubic_meter      2.500000            
```

## Practical Applications Included

### 1. Construction - Concrete Volume
Calculate concrete needed for foundations with automatic conversion to cubic meters.

### 2. Logistics - Container Capacity
Check if cargo fits in shipping containers by standardizing volumes.

### 3. Water Management - Tank Sizing
Size water storage tanks based on daily consumption requirements.

### 4. HVAC - Room Air Volume
Calculate air changes per hour for ventilation systems.

## Common Use Cases

### Construction
```python
# Foundation volume
length = 10 m × width = 8 m × depth = 0.3 m
Volume = 24 m³
```

### Logistics
```python
# Check container capacity
Container: 33.2 m³
Cargo: 1000 cubic_foot → 28.32 m³
Remaining: 4.88 m³
```

### Water Management
```python
# Tank sizing
Daily consumption: 5000 liters
Storage days: 3
Required: 15 m³ (15,000 liters)
```

### HVAC
```python
# Room ventilation
Room: 6m × 4m × 3m = 72 m³
ACH: 6 air changes/hour
Required airflow: 0.12 m³/s (254 CFM)
```

## Integration in Your Code

You can import and use the conversion function:

```python
from volume_to_cubic_meter import convert_to_cubic_meter

# Convert any volume to cubic meters
result = convert_to_cubic_meter(100, 'liter')

if result['success']:
    print(f"Volume in m³: {result['value_m3']}")
    print(f"Volume in liters: {result['value_liters']}")
else:
    print(f"Error: {result['error']}")
```

## Error Handling

The converter gracefully handles errors:

```
======================================================================
CONVERSION ERROR
======================================================================

Error: Cannot convert from invalid_unit to cubic_meter: ...
Message: Failed to convert 100 invalid_unit to cubic meters

Please check:
  • Unit spelling is correct
  • Unit is a volume unit (not length, mass, etc.)
  • Value is a valid number
======================================================================
```

## Why Cubic Meters?

Cubic meters (m³) is the SI unit for volume and is:
- **Universal**: Recognized worldwide
- **Standard**: Used in engineering and science
- **Convenient**: Easy to work with (1 m³ = 1000 liters)
- **Practical**: Suitable for both small and large volumes

## Conversion Reference

| Unit | To Cubic Meters |
|------|----------------|
| 1 liter | 0.001 m³ |
| 1 gallon (US) | 0.003785 m³ |
| 1 quart | 0.000946 m³ |
| 1 pint | 0.000473 m³ |
| 1 cup | 0.000237 m³ |
| 1 fluid ounce | 0.0000296 m³ |
| 1000 liters | 1 m³ |

## Tips

1. **Always specify units** - Don't assume default units
2. **Check spelling** - Use exact unit names from supported list
3. **Use help command** - Type 'help' in interactive mode
4. **Batch processing** - Use batch mode for multiple conversions
5. **Verify results** - Cross-check critical calculations

## Related Examples

- `unit_conversions_comprehensive.py` - All unit types
- `civil_engineering.py` - Construction volumes
- `hvac_mechanical.py` - Air volumes and flow rates
- `oil_and_gas.py` - Tank and pipeline volumes

## Contributing

To add more volume units or features:
1. Check if the unit is supported in Unifyt
2. Add to the supported units list
3. Test the conversion
4. Update documentation

## Support

For issues or questions:
- Check the main README.md
- Review Unifyt documentation
- See other examples in this directory

---

**Note**: This converter uses the Unifyt library for all conversions, ensuring accuracy and consistency with scientific standards.
