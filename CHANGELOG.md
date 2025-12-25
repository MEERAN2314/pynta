# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-12-24

### Added
- Initial release of Unifyt
- Core `Quantity` class for representing values with units
- `Unit` class for unit management and conversions
- `Dimension` class for tracking physical dimensions
- `UnitRegistry` for custom unit definitions
- `UnitContext` for unit system management
- Support for 100+ units including:
  - Basic SI units (length, mass, time, etc.)
  - Imperial units
  - Energy units (joule, calorie, kWh, eV)
  - Power units (watt, horsepower)
  - Pressure units (pascal, bar, atm, psi)
  - Force units (newton, pound_force)
  - Frequency units (hertz, MHz, GHz)
  - Voltage and electrical units
  - Volume units (liter, gallon)
  - Angle units (radian, degree)
- Physical constants module with 30+ constants:
  - Fundamental constants (c, h, G, k_B, etc.)
  - Astronomical constants (AU, ly, M_sun, etc.)
  - Atomic constants (a_0, m_e, m_p, etc.)
- Utility functions module:
  - Array creation (linspace, arange, zeros, ones, full)
  - Array operations (concatenate, stack)
  - Statistical functions (sum, mean, std, min, max)
  - Mathematical functions (sqrt, clip, isclose)
- Serialization support:
  - JSON serialization/deserialization
  - Pickle support
  - File save/load functions
  - Custom JSON encoder/decoder
- Performance optimizations:
  - Unit caching for faster parsing
  - Efficient dimension checking
  - NumPy vectorization
- Comprehensive test suite with 50+ tests
- Full documentation:
  - User guide with examples
  - Complete API reference
  - Performance guide
  - Migration guide from Pint/Unyt
  - Feature documentation
- Example scripts:
  - Basic usage examples
  - Scientific calculations
  - Custom unit definitions
  - Array operations
  - Advanced features (constants, utils, serialization)
- Development tools:
  - Setup script
  - Test runner
  - Code formatter
  - Code quality checker
- Type hints for better IDE support
- Full PEP 561 compliance

### Features
- Intuitive API for creating and manipulating quantities
- Automatic unit conversion in arithmetic operations
- Support for compound units (e.g., meter/second)
- Array operations with NumPy integration
- Custom unit definitions
- Unit system contexts
- Comparison operations
- Power operations
- Dimensionality checking
- Physical constants with proper units
- Utility functions for common operations
- Serialization to JSON and pickle

### Documentation
- User guide with comprehensive examples
- Complete API reference
- Quick start guide
- Performance optimization guide
- Migration guide from other libraries
- Contributing guidelines
- README with feature overview
- Inline documentation with docstrings

### Performance
- Unit caching reduces parsing overhead
- NumPy integration for vectorized operations
- Efficient dimension tracking
- Optimized conversion calculations
- 2-5x faster than Pint for array operations

[Unreleased]: https://github.com/yourusername/unifyt/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/unifyt/releases/tag/v0.1.0
