# Unit Conversion Examples - Complete Index

## Quick Navigation

| Industry | File | Key Topics | Common Units |
|----------|------|------------|--------------|
| **Aerospace** | `aerospace_engineering.py` | Aircraft, Rockets, Orbital Mechanics | knot, mach, psi, pound_force |
| **Oil & Gas** | `oil_and_gas.py` | Drilling, Production, Refining | barrel, MMSCFD, psi, API gravity |
| **Civil** | `civil_engineering.py` | Structures, Construction, Infrastructure | MPa, kN, m³, cubic_yard |
| **Electrical** | `electrical_power.py` | Generation, Transmission, Distribution | MW, kV, kWh, ampere |
| **HVAC** | `hvac_mechanical.py` | Cooling, Heating, Ventilation | ton, CFM, BTU/hr, COP |
| **Comprehensive** | `unit_conversions_comprehensive.py` | All Domains, 300+ Units | All units |

## By Use Case

### Design & Engineering
- **Structural Design**: `civil_engineering.py` → Sections 1-3, 8-9
- **Mechanical Design**: `hvac_mechanical.py` → All sections
- **Electrical Design**: `electrical_power.py` → Sections 2-4
- **Aircraft Design**: `aerospace_engineering.py` → Sections 1, 4-5

### Operations & Production
- **Oil Production**: `oil_and_gas.py` → Sections 2-3, 7
- **Power Generation**: `electrical_power.py` → Sections 1, 7-8
- **Flight Operations**: `aerospace_engineering.py` → Sections 1, 7-8
- **Building Operations**: `hvac_mechanical.py` → Sections 1-4, 7

### Construction & Installation
- **Building Construction**: `civil_engineering.py` → Sections 5, 9-10
- **Pipeline Installation**: `oil_and_gas.py` → Section 4
- **Electrical Installation**: `electrical_power.py` → Section 4
- **HVAC Installation**: `hvac_mechanical.py` → Sections 2, 5

### Testing & Commissioning
- **Well Testing**: `oil_and_gas.py` → Section 7
- **Structural Testing**: `civil_engineering.py` → Sections 1-3
- **Electrical Testing**: `electrical_power.py` → Section 6
- **HVAC Commissioning**: `hvac_mechanical.py` → Sections 7-8

## By Unit Type

### Pressure
- **High Pressure**: `oil_and_gas.py` (drilling, reservoir)
- **Medium Pressure**: `civil_engineering.py` (concrete, steel)
- **Low Pressure**: `hvac_mechanical.py` (duct, static)
- **Electrical**: `electrical_power.py` (not applicable)

### Temperature
- **High Temp**: `oil_and_gas.py` (refining), `aerospace_engineering.py` (combustion)
- **Medium Temp**: `civil_engineering.py` (pavement)
- **Comfort Range**: `hvac_mechanical.py` (all sections)
- **Cryogenic**: `aerospace_engineering.py` (propellants)

### Flow Rates
- **Liquid**: `oil_and_gas.py` (production, pipeline)
- **Gas**: `oil_and_gas.py` (gas production)
- **Air**: `hvac_mechanical.py` (ventilation)
- **Water**: `civil_engineering.py` (hydraulics)

### Energy & Power
- **Electrical**: `electrical_power.py` (all sections)
- **Thermal**: `hvac_mechanical.py` (heating, cooling)
- **Mechanical**: `aerospace_engineering.py` (propulsion)
- **Chemical**: `oil_and_gas.py` (fuel, combustion)

## Quick Reference Tables

### Most Common Conversions by Industry

#### Aerospace
```
Speed:      knot → km/h, m/s, mph
Altitude:   foot → meter, kilometer
Pressure:   psi → pascal, bar
Thrust:     pound_force → newton, kilonewton
```

#### Oil & Gas
```
Volume:     barrel → cubic_meter, liter, gallon
Flow:       bbl/day → m³/s, L/s
Pressure:   psi → MPa, bar, atmosphere
Gas:        MMSCFD → m³/s, m³/day
```

#### Civil Engineering
```
Strength:   MPa → psi, pascal
Force:      kN → newton, pound_force
Volume:     m³ → cubic_yard, liter
Area:       m² → foot², hectare
```

#### Electrical Power
```
Power:      MW → kW, W, GW
Voltage:    kV → volt, megavolt
Energy:     kWh → joule, MWh
Current:    ampere → kiloampere, milliampere
```

#### HVAC
```
Cooling:    ton → kW, BTU/hr
Flow:       CFM → m³/s, L/s
Pressure:   inWC → pascal, psi
Temp:       °C → °F, K
```

## Example Usage Patterns

### Pattern 1: Direct Conversion
```python
from unifyt import Quantity

# Simple conversion
pressure = Quantity(1000, 'psi')
pressure_mpa = pressure.to('megapascal')
print(f"{pressure} = {pressure_mpa}")
```

### Pattern 2: Calculation with Units
```python
from unifyt import Quantity

# Calculate with units
force = Quantity(5000, 'newton')
area = Quantity(0.01, 'meter^2')
pressure_value = force.magnitude / area.magnitude
pressure = Quantity(pressure_value, 'pascal')
print(f"Pressure: {pressure.to('megapascal')}")
```

### Pattern 3: Using Constants
```python
from unifyt import Quantity, constants

# Use physical constants
mass = Quantity(100, 'kilogram')
force_value = mass.magnitude * constants.g.magnitude
force = Quantity(force_value, 'newton')
print(f"Weight: {force}")
```

### Pattern 4: Array Operations
```python
from unifyt import Quantity
import numpy as np

# Array conversions
pressures = Quantity(np.array([1000, 2000, 3000]), 'psi')
pressures_mpa = pressures.to('megapascal')
print(f"Pressures: {pressures_mpa}")
```

## Running All Examples

To run all industry examples sequentially:

```bash
# Run all examples
for file in aerospace_engineering.py oil_and_gas.py civil_engineering.py electrical_power.py hvac_mechanical.py; do
    echo "Running $file..."
    python unit-convertions-examples/$file
    echo ""
done
```

Or run the comprehensive example:

```bash
python unit-convertions-examples/unit_conversions_comprehensive.py
```

## Tips for Industry Professionals

### Aerospace Engineers
- Always verify altitude units (feet vs meters)
- Check if speed is indicated airspeed (IAS) or true airspeed (TAS)
- Confirm pressure altitude vs density altitude

### Oil & Gas Engineers
- Verify if barrels are oil barrels (42 gal) or other
- Check if gas volumes are at standard conditions
- Confirm API gravity vs specific gravity

### Civil Engineers
- Verify if loads are service loads or factored loads
- Check if concrete strength is cylinder or cube strength
- Confirm if dimensions are nominal or actual

### Electrical Engineers
- Verify if power is active (kW) or apparent (kVA)
- Check if voltage is line-to-line or line-to-neutral
- Confirm if current is RMS or peak

### HVAC Engineers
- Verify if tons are refrigeration tons or mass tons
- Check if temperatures are dry bulb or wet bulb
- Confirm if flow is actual or standard conditions

## Troubleshooting

### Common Issues

**Issue**: "Cannot convert from X to Y: incompatible dimensions"
- **Solution**: Check that units have compatible dimensions (e.g., can't convert pressure to temperature)

**Issue**: Temperature conversion seems wrong
- **Solution**: Remember that temperature differences (ΔT) convert differently than absolute temperatures

**Issue**: Getting very large or very small numbers
- **Solution**: Choose appropriate unit prefixes (k, M, G for large; m, μ, n for small)

**Issue**: Compound units not working
- **Solution**: Use proper syntax: 'meter/second' or 'meter * second^-1'

## Additional Examples

For more examples, see:
- `../examples/` - Basic usage examples
- `../docs/` - Complete documentation
- `../final documents/UNITS_CATALOG.md` - All available units

## Contributing New Examples

To contribute industry-specific examples:

1. Identify common conversions in your industry
2. Create a new Python file following the existing structure
3. Include real-world scenarios and values
4. Add comprehensive comments
5. Update this INDEX.md and README.md
6. Test all conversions

## License

All examples are provided under the same MIT license as the Unifyt library.

---

**Last Updated**: December 2024  
**Unifyt Version**: 0.2.0  
**Total Examples**: 5 industry files + 1 comprehensive file
