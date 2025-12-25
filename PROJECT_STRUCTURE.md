# Unifyt Project Structure

```
unifyt/
│
├── unifyt/                      # Main package directory
│   ├── __init__.py            # Package initialization, exports main classes
│   ├── quantity.py            # Quantity class - core functionality
│   ├── unit.py                # Unit class - unit management
│   ├── dimensions.py          # Dimension class - dimensionality tracking
│   ├── unit_registry.py       # UnitRegistry - custom unit management
│   ├── context.py             # UnitContext - unit system contexts
│   └── py.typed               # PEP 561 marker for type hints
│
├── tests/                      # Test suite
│   ├── __init__.py            # Test package initialization
│   ├── conftest.py            # Pytest configuration and fixtures
│   ├── test_quantity.py       # Tests for Quantity class
│   ├── test_unit.py           # Tests for Unit class
│   ├── test_dimensions.py     # Tests for Dimension class
│   ├── test_unit_registry.py  # Tests for UnitRegistry class
│   └── test_context.py        # Tests for UnitContext class
│
├── examples/                   # Example scripts
│   ├── README.md              # Examples overview
│   ├── basic_usage.py         # Basic operations
│   ├── scientific_calculations.py  # Scientific examples
│   ├── custom_units.py        # Custom unit definitions
│   └── array_operations.py    # NumPy array examples
│
├── docs/                       # Documentation
│   ├── user_guide.md          # Comprehensive user guide
│   ├── api_reference.md       # Complete API documentation
│   └── FEATURES.md            # Feature list and descriptions
│
├── .gitignore                 # Git ignore patterns
├── setup.py                   # Package setup configuration
├── pyproject.toml             # Modern Python project configuration
├── requirements.txt           # Runtime dependencies
├── requirements-dev.txt       # Development dependencies
├── MANIFEST.in                # Package manifest for distribution
├── LICENSE                    # MIT License
├── README.md                  # Main project README
├── QUICKSTART.md              # Quick start guide
├── CHANGELOG.md               # Version history
├── CONTRIBUTING.md            # Contribution guidelines
└── PROJECT_STRUCTURE.md       # This file

```

## Directory Descriptions

### `/unifyt` - Main Package

The core library implementation:

- **quantity.py**: The `Quantity` class that represents values with units. Handles arithmetic operations, conversions, and comparisons.
- **unit.py**: The `Unit` class for unit management, parsing, and conversion factors.
- **dimensions.py**: The `Dimension` class for tracking physical dimensions (length, mass, time, etc.).
- **unit_registry.py**: The `UnitRegistry` class for defining custom units and aliases.
- **context.py**: The `UnitContext` class for managing unit system contexts.

### `/tests` - Test Suite

Comprehensive test coverage:

- Tests for each major class
- Edge case testing
- Array operation tests
- Integration tests
- Pytest fixtures and configuration

### `/examples` - Example Scripts

Practical usage examples:

- Basic operations and conversions
- Scientific calculations (physics, chemistry)
- Custom unit definitions
- Array operations with NumPy
- Real-world use cases

### `/docs` - Documentation

Complete documentation:

- User guide with tutorials
- API reference with all classes and methods
- Feature descriptions
- Best practices

## Key Files

### Configuration Files

- **setup.py**: Package metadata and dependencies for pip installation
- **pyproject.toml**: Modern Python project configuration (Black, isort, mypy, pytest)
- **requirements.txt**: Runtime dependencies (numpy)
- **requirements-dev.txt**: Development dependencies (pytest, black, mypy, etc.)
- **MANIFEST.in**: Files to include in distribution package

### Documentation Files

- **README.md**: Main project overview, installation, quick start
- **QUICKSTART.md**: 5-minute getting started guide
- **CHANGELOG.md**: Version history and changes
- **CONTRIBUTING.md**: Guidelines for contributors
- **LICENSE**: MIT License text

### Development Files

- **.gitignore**: Files and directories to exclude from git
- **py.typed**: Marker file indicating the package has type hints

## Module Dependencies

```
unifyt/__init__.py
    ├── imports: quantity.Quantity
    ├── imports: unit.Unit
    ├── imports: dimensions.Dimension
    ├── imports: unit_registry.UnitRegistry
    └── imports: context.UnitContext

unifyt/quantity.py
    ├── imports: unit.Unit
    ├── imports: dimensions.Dimension
    └── depends on: numpy

unifyt/unit.py
    ├── imports: dimensions.Dimension
    └── no external dependencies

unifyt/dimensions.py
    └── no external dependencies

unifyt/unit_registry.py
    ├── imports: unit.Unit
    └── no external dependencies

unifyt/context.py
    └── no external dependencies
```

## Installation Structure

When installed via pip, the package structure is:

```
site-packages/
└── unifyt/
    ├── __init__.py
    ├── quantity.py
    ├── unit.py
    ├── dimensions.py
    ├── unit_registry.py
    ├── context.py
    └── py.typed
```

## Development Workflow

1. **Setup**: Install with `pip install -e ".[dev]"`
2. **Code**: Edit files in `/unifyt`
3. **Test**: Run `pytest tests/`
4. **Format**: Run `black unifyt/ tests/`
5. **Lint**: Run `flake8 unifyt/`
6. **Type Check**: Run `mypy unifyt/`
7. **Document**: Update docs in `/docs`
8. **Example**: Add examples to `/examples`

## Distribution

Package is distributed via PyPI:

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Design Principles

1. **Simplicity**: Easy to use API
2. **Performance**: Optimized for speed with NumPy
3. **Safety**: Type hints and dimension checking
4. **Extensibility**: Custom units and registries
5. **Documentation**: Comprehensive docs and examples
