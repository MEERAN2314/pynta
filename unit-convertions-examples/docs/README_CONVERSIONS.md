# Comprehensive Unit Conversion Examples

This directory contains extensive examples demonstrating the full power of the Unifyt library's unit conversion capabilities.

## Files

### `unit_conversions_comprehensive.py`
A comprehensive demonstration file showcasing **300+ unit conversions** across multiple domains and complexity levels.

## What's Covered

### Part 1: Normal Conversions - Everyday Use
- **Length**: Metric ↔ Imperial conversions (meters, feet, inches, miles)
- **Mass/Weight**: Body weight, cooking measurements (kg, pounds, grams, ounces)
- **Temperature**: Room temperature, cooking, freezing point (Celsius, Fahrenheit, Kelvin)
- **Volume**: Liquid measurements (liters, gallons, cups, milliliters)
- **Speed**: Highway speeds, running pace (mph, km/h, m/s)
- **Time**: Work hours, movie durations (hours, minutes, seconds, days)
- **Energy**: Food calories, electricity bills (kcal, kWh, joules)

### Part 2: General Use Cases - Scientific & Engineering
- **Physics - Mechanics**: Acceleration, force, pressure
- **Physics - Energy & Power**: Kinetic energy, power output
- **Electromagnetic Units**: Voltage, current, capacitance, inductance, magnetic fields
- **Chemistry**: Concentration, molecular mass
- **Astronomy**: Astronomical distances (AU, light-years, parsecs), stellar masses
- **Atomic & Nuclear Physics**: Particle energy (eV, GeV), atomic scales (angstroms, femtometers)
- **Radioactivity & Radiation**: Activity (becquerel, curie), absorbed dose (gray, rad), equivalent dose (sievert, rem)
- **Data & Information**: File sizes (bytes, MB, GB, TB), binary units (KiB, MiB, GiB)

### Part 3: Industry-Level Scenarios - Professional Applications
- **Aerospace Engineering**: Rocket thrust, escape velocity, orbital mechanics
- **Civil Engineering**: Bridge loads, concrete strength, structural deflection
- **Automotive Engineering**: Engine power, torque, fuel efficiency, tire pressure
- **Chemical Engineering**: Flow rates, reactor pressure, viscosity, heat capacity
- **Electrical Power Engineering**: High voltage transmission, power plant output, grid operations
- **Oil & Gas Industry**: Well pressure, production rates, pipeline throughput
- **Pharmaceutical Industry**: Drug concentration, dosage, reaction temperature
- **Telecommunications**: 5G frequencies, data transfer rates, fiber optic cables
- **Mining & Metallurgy**: Ore processing, smelting temperature, deep mine pressure
- **Renewable Energy**: Solar irradiance, wind turbine power, panel efficiency

### Part 4: Advanced Conversions - Pushing the Limits
- **Extreme Scale Conversions**: Planck length to observable universe (10^-35 to 10^26 meters)
- **Time Scale Conversions**: Attoseconds to age of universe
- **Energy Scale Conversions**: Thermal energy to Planck energy
- **Compound Unit Conversions**: Momentum, angular momentum, power density, energy density
- **Multi-Step Conversions**: Chain conversions across multiple unit systems
- **Precision Conversions**: High-precision scientific calculations
- **Array-Based Conversions**: Bulk conversion of 10,000+ values (performance test)
- **Cross-Domain Conversions**: Wavelength ↔ energy, temperature ↔ energy, mass ↔ energy (E=mc²)
- **Dimensionless Conversions**: Percentages, ppm, ppb, angles
- **Real-World Complex Scenario**: Mars mission calculations (distance, speed, travel time, energy)

### Part 5: Specialized Industry Conversions
- **Aviation Industry**: Cruise altitude, airspeed, fuel consumption, cabin pressure
- **Marine Engineering**: Ship speed (knots), ocean depth (fathoms), hydrostatic pressure
- **Medical & Healthcare**: Blood pressure (mmHg), drug dosage, radiation dose limits
- **Food & Beverage Industry**: Fermentation temperature, batch volume, alcohol content
- **HVAC Engineering**: Cooling capacity (tons of refrigeration), air flow rate
- **Semiconductor Manufacturing**: Process node size (nanometers), wafer size, deposition rate
- **Agriculture**: Field area (hectares, acres), irrigation volume, fertilizer application
- **Construction & Architecture**: Building height, floor area, thermal conductivity
- **Textile Industry**: Thread count, fabric weight, dyeing temperature
- **Printing & Publishing**: Print resolution (DPI), paper weight, press speed

### Part 6: Edge Cases & Special Conversions
- **Very Small Numbers**: Quantum scale (Compton wavelength, proton radius)
- **Very Large Numbers**: Cosmological scale (Andromeda distance, Milky Way mass)
- **Temperature Extremes**: Absolute zero to Planck temperature
- **Frequency Extremes**: ELF radio to gamma rays
- **Pressure Extremes**: Ultra-high vacuum to Earth's core pressure
- **Speed Comparisons**: Snail to speed of light
- **Energy Density Comparisons**: Batteries to nuclear fuel

## Key Features Demonstrated

✅ **300+ unit conversions** across all domains  
✅ **80+ physical constants** with proper units  
✅ **10+ industry domains** with real-world scenarios  
✅ **Extreme scale handling**: 10^-35 to 10^26 meters  
✅ **Complex compound units**: momentum, energy density, power density  
✅ **Array-based bulk conversions**: 10,000+ values efficiently  
✅ **Multi-step calculations**: Interdisciplinary physics problems  
✅ **High precision**: Maintained across all scales  
✅ **Temperature offsets**: Proper Celsius/Fahrenheit/Kelvin handling  
✅ **Dimensionality checking**: Prevents invalid conversions  

## Running the Examples

```bash
# Run the comprehensive examples
python examples/unit_conversions_comprehensive.py

# The output will show:
# - All conversion examples organized by category
# - Original values and converted values
# - Real-world application scenarios
# - Performance metrics for bulk conversions
# - Summary statistics
```

## Library Improvements Made

During the creation of these examples, several improvements were made to the Unifyt library:

1. **Added missing unit mappings**: microampere, nanoampere, picoampere, kiloampere, and other advanced units
2. **Added missing units**: terajoule (TJ), cubic_meter (m³)
3. **Fixed dimensionality checking**: Ensured all units properly map to their base dimensions
4. **Added derived unit dimensions**: Added proper dimensions for watt, pascal, newton, hertz, volt, coulomb, ohm, farad, henry, tesla, weber, becquerel, gray, sievert, and more
5. **Fixed volume unit conversions**: Properly mapped liter to cubic_meter
6. **Resolved unit conflicts**: Handled ambiguous abbreviations (e.g., 'rad' for both radian and radiation absorbed dose)

## Use Cases

This comprehensive example file is perfect for:

- **Learning**: Understanding the full capabilities of Unifyt
- **Testing**: Verifying library functionality across all domains
- **Reference**: Quick lookup for conversion patterns
- **Validation**: Ensuring accuracy of conversions
- **Documentation**: Demonstrating real-world applications
- **Benchmarking**: Performance testing with large datasets

## Notes

- All conversions maintain high precision
- Temperature conversions properly handle offsets
- Compound units are calculated numerically to avoid parsing issues
- Array operations demonstrate vectorization performance
- Real-world scenarios use actual industry values

## Contributing

If you have additional conversion scenarios or industry use cases to add, please contribute! The goal is to showcase the full power and versatility of the Unifyt library.
