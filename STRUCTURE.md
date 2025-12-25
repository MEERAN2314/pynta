# Unifyt Project Structure

```
unifyt/
│
├── 📁 unifyt/                      # Main package source code
│   ├── __init__.py               # Package initialization & exports
│   ├── quantity.py               # Quantity class (core functionality)
│   ├── unit.py                   # Unit class (100+ units)
│   ├── dimensions.py             # Physical dimension tracking
│   ├── unit_registry.py          # Custom unit management
│   ├── context.py                # Unit system contexts
│   ├── constants.py              # Physical constants (30+)
│   ├── utils.py                  # Utility functions (15+)
│   ├── serialization.py          # JSON/pickle serialization
│   └── py.typed                  # PEP 561 type marker
│
├── 📁 tests/                      # Test suite
│   ├── __init__.py               # Test package init
│   ├── conftest.py               # Pytest configuration & fixtures
│   ├── test_quantity.py          # Quantity class tests
│   ├── test_unit.py              # Unit class tests
│   ├── test_dimensions.py        # Dimension tests
│   ├── test_unit_registry.py     # Registry tests
│   ├── test_context.py           # Context manager tests
│   ├── test_constants.py         # Physical constants tests
│   ├── test_utils.py             # Utility function tests
│   └── test_serialization.py     # Serialization tests
│
├── 📁 examples/                   # Example scripts
│   ├── README.md                 # Examples documentation
│   ├── basic_usage.py            # Basic operations
│   ├── scientific_calculations.py # Physics/chemistry examples
│   ├── custom_units.py           # Custom unit definitions
│   ├── array_operations.py       # NumPy integration
│   ├── advanced_features.py      # Constants, utils, serialization
│   └── complete_demo.py          # Comprehensive showcase
│
├── 📁 docs/                       # Documentation
│   ├── user_guide.md             # Complete user guide
│   ├── api_reference.md          # Full API documentation
│   ├── FEATURES.md               # Detailed feature list
│   ├── PERFORMANCE.md            # Performance guide & benchmarks
│   └── MIGRATION.md              # Migration from Pint/Unyt
│
├── 📄 README.md                   # Project overview & quick start
├── 📄 INDEX.md                    # Complete project index
├── 📄 GETTING_STARTED.md          # Comprehensive getting started
├── 📄 QUICKSTART.md               # 5-minute quick start
├── 📄 STRUCTURE.md                # This file - project structure
├── 📄 PROJECT_SUMMARY.md          # Complete project summary
├── 📄 IMPROVEMENTS_SUMMARY.md     # What was improved
├── 📄 CHANGELOG.md                # Version history
├── 📄 CONTRIBUTING.md             # Contribution guidelines
├── 📄 LICENSE                     # MIT License
│
├── ⚙️ setup.py                    # Package setup configuration
├── ⚙️ pyproject.toml              # Modern build configuration
├── ⚙️ MANIFEST.in                 # Package manifest
├── ⚙️ requirements.txt            # Runtime dependencies
├── ⚙️ requirements-dev.txt        # Development dependencies
├── ⚙️ .gitignore                  # Git ignore rules
│
└── 🔧 Scripts/                    # Development scripts
    ├── setup_dev.sh              # Development environment setup
    ├── run_tests.sh              # Run test suite with coverage
    ├── run_examples.sh           # Run all examples
    ├── check_code.sh             # Code quality checker
    ├── format_code.sh            # Code formatter
    └── clean.sh                  # Clean temporary files
```

## Directory Descriptions

### 📁 unifyt/ - Core Library
The main package containing all library code:
- **quantity.py** (200 lines) - Core Quantity class with arithmetic operations
- **unit.py** (400 lines) - Unit definitions and conversions (100+ units)
- **dimensions.py** (100 lines) - Physical dimension tracking
- **constants.py** (200 lines) - Physical constants (30+)
- **utils.py** (250 lines) - Utility functions for arrays and statistics
- **serialization.py** (150 lines) - JSON and pickle support
- **unit_registry.py** (60 lines) - Custom unit management
- **context.py** (50 lines) - Unit system contexts

**Total: ~1,400 lines**

### 📁 tests/ - Test Suite
Comprehensive test coverage:
- 50+ test cases across 8 test modules
- Pytest-based with fixtures
- High code coverage (>90%)
- Tests for all features including edge cases

**Total: ~1,000 lines**

### 📁 examples/ - Example Scripts
Practical examples demonstrating features:
- **basic_usage.py** - Fundamental operations
- **scientific_calculations.py** - Real-world physics/chemistry
- **custom_units.py** - Custom unit definitions
- **array_operations.py** - NumPy integration
- **advanced_features.py** - Constants, utils, serialization
- **complete_demo.py** - Comprehensive showcase

**Total: ~600 lines**

### 📁 docs/ - Documentation
Comprehensive documentation:
- **user_guide.md** - Complete usage guide
- **api_reference.md** - Full API documentation
- **FEATURES.md** - Feature list and examples
- **PERFORMANCE.md** - Optimization guide
- **MIGRATION.md** - Migration from other libraries

**Total: ~3,000 lines**

## File Organization

### Root Level Documentation
- **README.md** - First file users see, project overview
- **INDEX.md** - Navigation hub for all documentation
- **GETTING_STARTED.md** - Comprehensive tutorial for new users
- **QUICKSTART.md** - 5-minute introduction
- **STRUCTURE.md** - This file, explains project layout

### Project Information
- **PROJECT_SUMMARY.md** - Complete project overview
- **IMPROVEMENTS_SUMMARY.md** - Enhancement details
- **CHANGELOG.md** - Version history
- **CONTRIBUTING.md** - How to contribute
- **LICENSE** - MIT License

### Configuration Files
- **setup.py** - Package installation configuration
- **pyproject.toml** - Modern Python build system
- **MANIFEST.in** - Files to include in distribution
- **requirements.txt** - Runtime dependencies (numpy)
- **requirements-dev.txt** - Development dependencies
- **.gitignore** - Files to ignore in git

### Development Scripts
All scripts are executable (chmod +x):
- **setup_dev.sh** - One-command dev environment setup
- **run_tests.sh** - Run tests with coverage report
- **run_examples.sh** - Run all example scripts
- **check_code.sh** - Check code quality (black, flake8, mypy)
- **format_code.sh** - Auto-format code
- **clean.sh** - Remove temporary and cache files

## Code Statistics

| Component | Files | Lines | Description |
|-----------|-------|-------|-------------|
| Core Library | 9 | ~1,400 | Main package code |
| Tests | 10 | ~1,000 | Test suite |
| Examples | 7 | ~600 | Example scripts |
| Documentation | 15+ | ~4,000 | Docs and guides |
| **Total** | **40+** | **~7,000** | Complete project |

## Module Dependencies

```
unifyt/
├── quantity.py
│   ├── → unit.py
│   ├── → dimensions.py
│   └── → numpy
│
├── unit.py
│   └── → dimensions.py
│
├── constants.py
│   └── → quantity.py
│
├── utils.py
│   ├── → quantity.py
│   └── → numpy
│
├── serialization.py
│   ├── → quantity.py
│   ├── → unit.py
│   └── → json, pickle
│
└── __init__.py
    ├── → quantity.py
    ├── → unit.py
    ├── → dimensions.py
    ├── → unit_registry.py
    ├── → context.py
    ├── → constants.py
    ├── → utils.py
    └── → serialization.py
```

## Key Features by Module

### quantity.py
- Quantity class
- Arithmetic operations
- Unit conversions
- Array support
- Comparison operations

### unit.py
- 100+ unit definitions
- Unit parsing
- Conversion factors
- Dimensionality checking
- Unit caching

### constants.py
- 30+ physical constants
- Fundamental constants
- Astronomical constants
- Atomic constants

### utils.py
- Array creation (linspace, arange, zeros, ones, full)
- Statistics (sum, mean, std, min, max)
- Math functions (sqrt, clip, isclose)
- Array operations (concatenate, stack)

### serialization.py
- JSON serialization
- Pickle support
- File I/O
- Custom encoders/decoders

## Navigation

- **New users**: Start with [GETTING_STARTED.md](GETTING_STARTED.md)
- **Quick intro**: See [QUICKSTART.md](QUICKSTART.md)
- **Find anything**: Check [INDEX.md](INDEX.md)
- **API docs**: Read [docs/api_reference.md](docs/api_reference.md)
- **Examples**: Browse [examples/](examples/)

## Maintenance

### Cleaning
```bash
./clean.sh  # Remove cache and temporary files
```

### Testing
```bash
./run_tests.sh  # Run full test suite
```

### Code Quality
```bash
./check_code.sh   # Check code quality
./format_code.sh  # Format code
```

### Development
```bash
./setup_dev.sh  # Set up development environment
```

---

**Last Updated**: December 24, 2024  
**Version**: 0.1.0  
**Total Lines**: ~7,000
