# Universal Converters Suite

## Overview

Three powerful, user-friendly converters that work flawlessly for both general users and industry professionals. Each converter provides instant conversions with real-world context and practical applications.

## The Three Universal Converters

### 1. 🌡️ Temperature Converter (`temperature_converter.py`)
Convert between Celsius, Fahrenheit, and Kelvin with real-world context.

**Features:**
- Instant conversion to all temperature scales
- Real-world context (e.g., "Room temperature", "Boiling point")
- Reference table with common temperatures
- Interactive and command-line modes

**Usage:**
```bash
# Interactive mode
python temperature_converter.py

# Direct conversion
python temperature_converter.py 25 C
# Output: 25°C = 77°F = 298.15K

# Show reference table
python temperature_converter.py --ref
```

**Perfect for:**
- Cooking and baking
- Weather forecasts
- Scientific experiments
- HVAC systems
- International travel

---

### 2. 🚗 Speed Converter (`speed_converter.py`)
Convert between all speed units with travel time calculator.

**Features:**
- Convert mph, km/h, m/s, knots, fps
- Real-world context (e.g., "Highway driving", "Jet aircraft")
- Travel time calculator
- Reference table from walking to speed of light
- Interactive mode

**Usage:**
```bash
# Interactive mode
python speed_converter.py

# Direct conversion
python speed_converter.py 60 mph
# Output: 60 mph = 96.56 km/h = 26.82 m/s

# Show reference table
python speed_converter.py --ref

# Calculate travel time (in interactive mode)
> time
Enter distance: 100 km
Enter speed: 60 mph
# Output: Travel time: 1.04 hours (62.1 minutes)
```

**Perfect for:**
- Travel planning
- Vehicle specifications
- Sports and athletics
- Aviation and marine
- Scientific calculations

---

### 3. 💨 Pressure Converter (`pressure_converter.py`)
Convert between all pressure units with altitude calculator.

**Features:**
- Convert Pa, kPa, MPa, bar, atm, psi, torr, mmHg
- Real-world context (e.g., "Tire pressure", "Sea level")
- Altitude pressure calculator
- Tire pressure guide
- Reference table

**Usage:**
```bash
# Interactive mode
python pressure_converter.py

# Direct conversion
python pressure_converter.py 100 kpa
# Output: 100 kPa = 1 bar = 14.5 psi = 0.987 atm

# Show reference table
python pressure_converter.py --ref

# Show tire pressure guide
python pressure_converter.py --tire

# Calculate pressure at altitude (in interactive mode)
> alt
Enter altitude: 1000 m
# Output: Estimated pressure at 1000m altitude
```

**Perfect for:**
- Weather forecasting
- Tire maintenance
- Scuba diving
- Aviation
- Engineering applications

---

## Common Features

All three converters share these features:

✅ **Interactive Mode** - User-friendly prompts and guidance  
✅ **Command-Line Mode** - Quick conversions from terminal  
✅ **Real-World Context** - Understand what the numbers mean  
✅ **Reference Tables** - Common values for quick lookup  
✅ **Error Handling** - Clear error messages and suggestions  
✅ **Multiple Units** - Convert to all relevant units at once  
✅ **Help System** - Built-in help and examples  

## Quick Start Guide

### Installation
No installation needed! Just have Unifyt installed:
```bash
pip install unifyt
```

### Basic Usage Pattern

All converters follow the same pattern:

```bash
# Interactive mode (easiest for beginners)
python <converter>.py

# Direct conversion (fastest for quick lookups)
python <converter>.py <value> <unit>

# Show reference table
python <converter>.py --ref

# Show help
python <converter>.py --help
```

### Examples

#### Temperature
```bash
# Cooking: Convert oven temperature
python temperature_converter.py 350 F
# Result: 176.67°C

# Weather: Convert forecast
python temperature_converter.py 25 C
# Result: 77°F

# Science: Convert to Kelvin
python temperature_converter.py 100 C
# Result: 373.15K
```

#### Speed
```bash
# Driving: Convert speed limit
python speed_converter.py 65 mph
# Result: 104.6 km/h

# Running: Convert pace
python speed_converter.py 10 kmh
# Result: 6.21 mph = 2.78 m/s

# Aviation: Convert airspeed
python speed_converter.py 500 knot
# Result: 926 km/h = 257 m/s
```

#### Pressure
```bash
# Tires: Convert tire pressure
python pressure_converter.py 32 psi
# Result: 220.6 kPa = 2.21 bar

# Weather: Convert barometric pressure
python pressure_converter.py 1013 mbar
# Result: 101.3 kPa = 1 atm

# Diving: Convert depth pressure
python pressure_converter.py 3 atm
# Result: 303.98 kPa = 44.1 psi
```

## Interactive Mode Features

### Temperature Converter
```
Commands:
- ref     : Show reference table
- quit    : Exit

Example session:
> 25 C
Result: 25°C = 77°F = 298.15K
Context: Room temperature (comfortable)

> 100 C
Result: 100°C = 212°F = 373.15K
Context: Boiling point of water
```

### Speed Converter
```
Commands:
- ref     : Show reference table
- time    : Calculate travel time
- quit    : Exit

Example session:
> 60 mph
Result: 60 mph = 96.56 km/h = 26.82 m/s
Context: Highway driving

> time
Distance: 100 km
Speed: 60 mph
Result: 1.04 hours (62.1 minutes)
```

### Pressure Converter
```
Commands:
- ref     : Show reference table
- alt     : Calculate altitude pressure
- tire    : Show tire pressure guide
- quit    : Exit

Example session:
> 32 psi
Result: 32 psi = 220.6 kPa = 2.21 bar
Context: Moderate pressure (tire pressure)

> alt
Altitude: 1000 m
Result: 89.9 kPa = 0.887 atm
```

## Real-World Applications

### For General Users

#### Temperature
- **Cooking**: Convert recipe temperatures
- **Travel**: Understand weather forecasts abroad
- **Home**: Set thermostat correctly
- **Health**: Understand body temperature readings

#### Speed
- **Driving**: Understand speed limits abroad
- **Fitness**: Track running/cycling pace
- **Travel**: Calculate trip duration
- **Sports**: Compare athlete speeds

#### Pressure
- **Car Maintenance**: Check tire pressure
- **Weather**: Understand barometric pressure
- **Cooking**: Pressure cooker settings
- **Health**: Blood pressure context

### For Industry Professionals

#### Temperature
- **HVAC**: System design and troubleshooting
- **Manufacturing**: Process temperature control
- **Food Industry**: Safety compliance
- **Research**: Scientific experiments

#### Speed
- **Transportation**: Vehicle specifications
- **Aviation**: Flight planning
- **Marine**: Navigation calculations
- **Engineering**: Fluid dynamics

#### Pressure
- **Engineering**: System design
- **Aviation**: Altitude calculations
- **Diving**: Depth pressure planning
- **Manufacturing**: Hydraulic systems

## Tips and Tricks

### Temperature
1. **Cooking**: Most ovens use Fahrenheit in US, Celsius elsewhere
2. **Weather**: 0°C = freezing, 20°C = room temp, 30°C = hot
3. **Science**: Always use Kelvin for calculations
4. **Quick estimate**: °F ≈ (°C × 2) + 30 (rough approximation)

### Speed
1. **Quick conversion**: 100 km/h ≈ 62 mph
2. **Walking**: ~5 km/h or 3 mph
3. **Highway**: 100-120 km/h or 60-75 mph
4. **Sound**: ~1235 km/h or 767 mph at sea level

### Pressure
1. **Sea level**: 101.325 kPa = 1 atm = 14.7 psi
2. **Tire pressure**: Usually 30-35 psi for cars
3. **Altitude**: Pressure drops ~12% per 1000m
4. **Weather**: High pressure = good weather, low = storms

## Error Handling

All converters provide clear error messages:

```bash
# Invalid unit
> python temperature_converter.py 25 X
Error: Unknown unit: X
Use celsius, fahrenheit, or kelvin

# Invalid value
> python speed_converter.py abc mph
Error: First argument must be a number

# Missing unit
> python pressure_converter.py 100
Error: Enter both value and unit (e.g., '100 kpa')
```

## Integration in Your Code

You can import and use these converters in your own Python code:

```python
from temperature_converter import convert_temperature
from speed_converter import convert_speed
from pressure_converter import convert_pressure

# Temperature
temp_result = convert_temperature(25, 'celsius')
if temp_result['success']:
    print(f"Fahrenheit: {temp_result['fahrenheit_val']:.1f}°F")

# Speed
speed_result = convert_speed(60, 'mph')
if speed_result['success']:
    print(f"km/h: {speed_result['kmh_val']:.1f}")

# Pressure
pressure_result = convert_pressure(100, 'kpa')
if pressure_result['success']:
    print(f"PSI: {pressure_result['psi_val']:.1f}")
```

## Comparison with Other Tools

### Why Use These Converters?

✅ **Offline**: No internet required  
✅ **Fast**: Instant results  
✅ **Context**: Real-world meaning  
✅ **Accurate**: Based on Unifyt library  
✅ **Free**: No cost, no ads  
✅ **Simple**: Easy to use  
✅ **Comprehensive**: All units in one place  

### vs. Online Converters
- ✅ Works offline
- ✅ No ads or tracking
- ✅ Faster (no page loading)
- ✅ Batch conversions
- ✅ Programmable

### vs. Calculator Apps
- ✅ More units supported
- ✅ Real-world context
- ✅ Reference tables
- ✅ Special calculators (travel time, altitude)

## Troubleshooting

### Common Issues

**Issue**: "Command not found"
- **Solution**: Make sure you're in the correct directory
- Run: `cd unit-convertions-examples`

**Issue**: "Module not found: unifyt"
- **Solution**: Install Unifyt
- Run: `pip install unifyt`

**Issue**: Conversion seems wrong
- **Solution**: Check unit spelling
- Use `--help` to see supported units

**Issue**: Interactive mode not working
- **Solution**: Make sure Python 3.8+ is installed
- Try command-line mode instead

## Future Enhancements

Planned features:
- [ ] History of recent conversions
- [ ] Favorite/bookmarked conversions
- [ ] Batch file processing
- [ ] GUI version
- [ ] Mobile app version
- [ ] API endpoint

## Contributing

Want to improve these converters?
1. Add more reference points
2. Improve context descriptions
3. Add more special calculators
4. Translate to other languages
5. Create GUI version

## Support

For help:
- Run with `--help` flag
- Check main README.md
- Review Unifyt documentation
- See other examples in this directory

---

**Note**: These converters are designed to be simple, fast, and accurate. They use the Unifyt library for all conversions, ensuring scientific accuracy and consistency.

**Version**: 1.0  
**Last Updated**: December 2024  
**License**: MIT (same as Unifyt)
