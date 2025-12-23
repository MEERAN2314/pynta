# Pynta

A powerful and easy-to-use Python library for unit conversion and calculations, combining the best features of Pint and Unyt.

## Features

- **Intuitive API**: Simple and Pythonic interface for working with physical quantities
- **Extensive Unit Support**: 100+ units including SI, imperial, energy, power, pressure, and more
- **High Performance**: Optimized for speed with caching and NumPy integration
- **Type Safety**: Full type hints for better IDE support
- **Flexible Conversions**: Easy unit conversions with automatic dimensionality checking
- **Array Support**: Seamless integration with NumPy arrays
- **Custom Units**: Define your own units and unit systems
- **Context Management**: Switch between unit systems easily
- **Physical Constants**: Built-in library of physical and astronomical constants
- **Utility Functions**: Array creation, statistical operations, and more
- **Serialization**: Save and load quantities in JSON or pickle format

## Installation

```bash
pip install pynta
```

## Quick Start

```python
from pynta import Quantity, constants, utils
import numpy as np

# Create quantities with units
distance = Quantity(100, 'meters')
time = Quantity(9.58, 'seconds')

# Perform calculations
speed = distance / time
print(speed)  # 10.438413361169102 meter / second

# Convert units
speed_mph = speed.to('miles/hour')
print(speed_mph)  # 23.350065963060686 mile / hour

# Work with arrays
distances = Quantity(np.array([100, 200, 300]), 'meters')
print(distances.to('kilometers'))  # [0.1 0.2 0.3] kilometer

# Use physical constants
mass = Quantity(1, 'kilogram')
energy = mass * constants.c ** 2  # E = mc²
print(energy.to('kilowatt_hour'))

# Utility functions
temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
mean_temp = utils.mean(temps)
```

## Documentation

### 📚 Getting Started
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Comprehensive tutorial
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute introduction
- **[INDEX.md](INDEX.md)** - Complete navigation hub

### 📖 User Documentation
- **[docs/user_guide.md](docs/user_guide.md)** - Complete usage guide
- **[docs/api_reference.md](docs/api_reference.md)** - Full API reference
- **[docs/FEATURES.md](docs/FEATURES.md)** - Detailed feature list
- **[examples/](examples/)** - Practical examples

### 🔧 Advanced Topics
- **[docs/PERFORMANCE.md](docs/PERFORMANCE.md)** - Optimization guide
- **[docs/MIGRATION.md](docs/MIGRATION.md)** - Migrating from Pint/Unyt

### 📋 Project Information
- **[STRUCTURE.md](STRUCTURE.md)** - Project structure
- **[ORGANIZATION.md](ORGANIZATION.md)** - How the project is organized
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete overview
- **[IMPROVEMENTS_SUMMARY.md](IMPROVEMENTS_SUMMARY.md)** - What was improved

## Examples

Check out the `examples/` directory for more usage examples:

- **basic_usage.py** - Basic unit conversions and operations
- **scientific_calculations.py** - Physics, chemistry, and engineering examples
- **custom_units.py** - Define your own units
- **array_operations.py** - NumPy array integration
- **advanced_features.py** - Constants, utilities, and serialization

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/MEERAN2314/pynta.git
cd pynta

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Run linting
flake8 pynta/

# Run type checking
mypy pynta/

# Format code
black pynta/ tests/
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Supported Units

### Core Units
- **Length**: meter, kilometer, mile, foot, inch, nanometer, angstrom, etc.
- **Mass**: kilogram, gram, pound, ounce, ton, etc.
- **Time**: second, minute, hour, day, week, year, millisecond, etc.
- **Temperature**: kelvin, celsius, fahrenheit

### Derived Units
- **Energy**: joule, calorie, kilowatt_hour, electronvolt, etc.
- **Power**: watt, kilowatt, horsepower, etc.
- **Pressure**: pascal, bar, atmosphere, psi, torr, etc.
- **Force**: newton, pound_force, etc.
- **Frequency**: hertz, kilohertz, megahertz, gigahertz
- **Voltage**: volt, millivolt, kilovolt
- **Volume**: liter, gallon, milliliter, cup, etc.
- **Angle**: radian, degree
- And many more!

## Physical Constants

Access fundamental constants with proper units:

```python
from pynta import constants

print(constants.c)          # Speed of light
print(constants.h)          # Planck constant
print(constants.G)          # Gravitational constant
print(constants.N_A)        # Avogadro number
print(constants.g)          # Standard gravity
print(constants.AU)         # Astronomical unit
print(constants.M_sun)      # Solar mass
```

## Acknowledgments

This library is inspired by and builds upon the excellent work of:
- [Pint](https://github.com/hgrecco/pint) - Python units library
- [Unyt](https://github.com/yt-project/unyt) - Handle, manipulate, and convert data with units

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.
