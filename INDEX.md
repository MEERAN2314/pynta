# Pynta Library - Complete Index

Welcome to Pynta! This index will help you find exactly what you need.

## 🚀 Quick Links

- **New User?** Start with [GETTING_STARTED.md](GETTING_STARTED.md)
- **5-Minute Intro?** Read [QUICKSTART.md](QUICKSTART.md)
- **Want Examples?** Check [examples/](examples/)
- **Need API Docs?** See [docs/api_reference.md](docs/api_reference.md)
- **Performance Tips?** Read [docs/PERFORMANCE.md](docs/PERFORMANCE.md)

## 📚 Documentation

### Getting Started
- [GETTING_STARTED.md](GETTING_STARTED.md) - Comprehensive getting started guide
- [QUICKSTART.md](QUICKSTART.md) - 5-minute quick start
- [README.md](README.md) - Project overview and features

### User Documentation
- [docs/user_guide.md](docs/user_guide.md) - Complete user guide
- [docs/api_reference.md](docs/api_reference.md) - Full API documentation
- [docs/FEATURES.md](docs/FEATURES.md) - Detailed feature list

### Advanced Topics
- [docs/PERFORMANCE.md](docs/PERFORMANCE.md) - Performance optimization guide
- [docs/MIGRATION.md](docs/MIGRATION.md) - Migrating from Pint/Unyt

### Project Information
- [STRUCTURE.md](STRUCTURE.md) - Project structure and layout
- [ORGANIZATION.md](ORGANIZATION.md) - How the project is organized
- [CHECKLIST.md](CHECKLIST.md) - Quality and maintenance checklists
- [CLEAN_PROJECT_SUMMARY.md](CLEAN_PROJECT_SUMMARY.md) - Clean project overview
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Complete project overview
- [IMPROVEMENTS_SUMMARY.md](IMPROVEMENTS_SUMMARY.md) - What's been improved
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [LICENSE](LICENSE) - MIT License

## 💻 Code

### Core Library (`pynta/`)
- [pynta/__init__.py](pynta/__init__.py) - Package initialization
- [pynta/quantity.py](pynta/quantity.py) - Quantity class (core functionality)
- [pynta/unit.py](pynta/unit.py) - Unit class (100+ units)
- [pynta/dimensions.py](pynta/dimensions.py) - Dimension tracking
- [pynta/unit_registry.py](pynta/unit_registry.py) - Custom unit management
- [pynta/context.py](pynta/context.py) - Unit system contexts
- [pynta/constants.py](pynta/constants.py) - Physical constants (30+)
- [pynta/utils.py](pynta/utils.py) - Utility functions (15+)
- [pynta/serialization.py](pynta/serialization.py) - JSON/pickle support

### Tests (`tests/`)
- [tests/test_quantity.py](tests/test_quantity.py) - Quantity tests
- [tests/test_unit.py](tests/test_unit.py) - Unit tests
- [tests/test_dimensions.py](tests/test_dimensions.py) - Dimension tests
- [tests/test_unit_registry.py](tests/test_unit_registry.py) - Registry tests
- [tests/test_context.py](tests/test_context.py) - Context tests
- [tests/test_constants.py](tests/test_constants.py) - Constants tests
- [tests/test_utils.py](tests/test_utils.py) - Utility tests
- [tests/test_serialization.py](tests/test_serialization.py) - Serialization tests

### Examples (`examples/`)
- [examples/basic_usage.py](examples/basic_usage.py) - Basic operations
- [examples/scientific_calculations.py](examples/scientific_calculations.py) - Physics/chemistry
- [examples/custom_units.py](examples/custom_units.py) - Custom unit definitions
- [examples/array_operations.py](examples/array_operations.py) - NumPy integration
- [examples/advanced_features.py](examples/advanced_features.py) - Constants, utils, serialization
- [examples/complete_demo.py](examples/complete_demo.py) - Comprehensive showcase
- [examples/README.md](examples/README.md) - Examples overview

## 🛠️ Development

### Setup & Configuration
- [setup.py](setup.py) - Package setup
- [pyproject.toml](pyproject.toml) - Build configuration
- [requirements.txt](requirements.txt) - Runtime dependencies
- [requirements-dev.txt](requirements-dev.txt) - Development dependencies
- [MANIFEST.in](MANIFEST.in) - Package manifest
- [.gitignore](.gitignore) - Git ignore rules

### Development Scripts
- [setup_dev.sh](setup_dev.sh) - Set up development environment
- [run_tests.sh](run_tests.sh) - Run test suite with coverage
- [run_examples.sh](run_examples.sh) - Run all examples
- [check_code.sh](check_code.sh) - Check code quality
- [format_code.sh](format_code.sh) - Format code automatically

## 📖 Learning Path

### For Beginners
1. Read [GETTING_STARTED.md](GETTING_STARTED.md)
2. Try [examples/basic_usage.py](examples/basic_usage.py)
3. Explore [QUICKSTART.md](QUICKSTART.md)
4. Review [docs/user_guide.md](docs/user_guide.md)

### For Scientists/Engineers
1. Check [examples/scientific_calculations.py](examples/scientific_calculations.py)
2. Review [pynta/constants.py](pynta/constants.py) for constants
3. Read [docs/FEATURES.md](docs/FEATURES.md)
4. Explore [examples/advanced_features.py](examples/advanced_features.py)

### For Data Analysts
1. Study [examples/array_operations.py](examples/array_operations.py)
2. Learn [pynta/utils.py](pynta/utils.py) utilities
3. Check [docs/PERFORMANCE.md](docs/PERFORMANCE.md)
4. Review statistical functions

### For Developers
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
3. Check test files in [tests/](tests/)
4. Study [docs/api_reference.md](docs/api_reference.md)

## 🔍 Find By Topic

### Units
- **Basic units**: [pynta/unit.py](pynta/unit.py) - Lines 20-150
- **Unit conversions**: [docs/user_guide.md](docs/user_guide.md) - "Unit Conversions"
- **Custom units**: [examples/custom_units.py](examples/custom_units.py)
- **All supported units**: [README.md](README.md) - "Supported Units"

### Constants
- **Physical constants**: [pynta/constants.py](pynta/constants.py)
- **Using constants**: [examples/advanced_features.py](examples/advanced_features.py)
- **Constants list**: [docs/api_reference.md](docs/api_reference.md) - "Constants"

### Arrays
- **Array operations**: [examples/array_operations.py](examples/array_operations.py)
- **NumPy integration**: [docs/user_guide.md](docs/user_guide.md) - "Array Operations"
- **Utility functions**: [pynta/utils.py](pynta/utils.py)

### Calculations
- **Physics**: [examples/scientific_calculations.py](examples/scientific_calculations.py)
- **Engineering**: [docs/user_guide.md](docs/user_guide.md) - "Engineering Applications"
- **Data analysis**: [examples/array_operations.py](examples/array_operations.py)

### Performance
- **Optimization guide**: [docs/PERFORMANCE.md](docs/PERFORMANCE.md)
- **Benchmarks**: [docs/PERFORMANCE.md](docs/PERFORMANCE.md) - "Benchmarks"
- **Tips**: [docs/PERFORMANCE.md](docs/PERFORMANCE.md) - "Performance Tips"

### Serialization
- **JSON/Pickle**: [pynta/serialization.py](pynta/serialization.py)
- **Examples**: [examples/advanced_features.py](examples/advanced_features.py)
- **API**: [docs/api_reference.md](docs/api_reference.md) - "Serialization"

## 🎯 Common Tasks

### Installation
```bash
pip install pynta
# or
./setup_dev.sh
```
See: [GETTING_STARTED.md](GETTING_STARTED.md)

### Running Tests
```bash
./run_tests.sh
# or
pytest tests/
```
See: [CONTRIBUTING.md](CONTRIBUTING.md)

### Running Examples
```bash
./run_examples.sh
# or
python examples/basic_usage.py
```
See: [examples/README.md](examples/README.md)

### Code Quality
```bash
./check_code.sh
# or
./format_code.sh
```
See: [CONTRIBUTING.md](CONTRIBUTING.md)

## 📊 Statistics

- **Total files**: 50+
- **Python code**: ~3,000 lines
- **Test code**: ~1,000 lines
- **Documentation**: ~4,000 lines
- **Examples**: ~600 lines
- **Units supported**: 100+
- **Physical constants**: 30+
- **Utility functions**: 15+
- **Test cases**: 50+

## 🔗 External Resources

### Similar Libraries
- [Pint](https://github.com/hgrecco/pint) - Python units library
- [Unyt](https://github.com/yt-project/unyt) - Units for yt

### Python Resources
- [NumPy Documentation](https://numpy.org/doc/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pytest Documentation](https://docs.pytest.org/)

## 💡 Tips

- **New to Pynta?** Start with [GETTING_STARTED.md](GETTING_STARTED.md)
- **Need quick help?** Check [QUICKSTART.md](QUICKSTART.md)
- **Looking for examples?** Browse [examples/](examples/)
- **Want to contribute?** Read [CONTRIBUTING.md](CONTRIBUTING.md)
- **Performance issues?** See [docs/PERFORMANCE.md](docs/PERFORMANCE.md)
- **Migrating from Pint/Unyt?** Read [docs/MIGRATION.md](docs/MIGRATION.md)

## 📞 Support

- **Documentation**: Check this index and linked files
- **Examples**: See [examples/](examples/) directory
- **Issues**: Open a GitHub issue
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🎉 Quick Start

```python
from pynta import Quantity, constants, utils

# Basic usage
distance = Quantity(100, 'meter')
print(distance.to('kilometer'))

# Use constants
energy = Quantity(1, 'kilogram') * constants.c ** 2

# Array operations
temps = utils.linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
print(utils.mean(temps))
```

For more, see [QUICKSTART.md](QUICKSTART.md)

---

**Last Updated**: December 24, 2024  
**Version**: 0.1.0  
**License**: MIT
