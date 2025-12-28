# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2024-12-29

### Added - Major Feature Release 🚀

#### New Core Features

**Uncertain Quantities** (`unifyt.uncertainty`):
- `UncertainQuantity` class for measurements with error margins
- Automatic uncertainty propagation in all arithmetic operations
- Support for both absolute and relative uncertainties
- Proper error propagation following standard formulas:
  - Addition/Subtraction: σ = √(σ₁² + σ₂²)
  - Multiplication/Division: σᵣₑₗ = √(σᵣₑₗ,₁² + σᵣₑₗ,₂²)
  - Power: σᵣₑₗ = |n| × σᵣₑₗ,ₓ
- Unit conversions preserve uncertainties
- Examples: experimental physics, measurement analysis

**Advanced Formatting** (`unifyt.formatter`):
- `QuantityFormatter` class with multiple output styles
- Supported formats:
  - `default`: Standard text output
  - `latex`: LaTeX mathematical notation
  - `unicode`: Unicode with superscripts/subscripts
  - `html`: HTML with proper markup
  - `compact`: Space-efficient notation
  - `scientific`: Scientific notation
- Configurable precision and formatting options
- Quick `format_quantity()` function for one-off formatting

**Unit Validation** (`unifyt.validator`):
- `UnitValidator` class for comprehensive unit checking
- `validate_unit()`: Check if unit string is valid
- `suggest_unit()`: Get suggestions for typos using Levenshtein distance
- `check_dimensionality()`: Verify unit compatibility
- `simplify_unit()`: Automatically simplify complex unit expressions
- `parse_compound_unit()`: Break down compound units into components
- Helpful error messages with correction suggestions

**Batch Operations** (`unifyt.batch`):
- `BatchConverter` class for processing multiple quantities
- `convert_all()`: Convert list of quantities to same unit
- `convert_dict()`: Convert dictionary of quantities
- `sum_quantities()`: Sum multiple compatible quantities
- `mean_quantities()`: Calculate mean of quantities
- `min_quantity()` / `max_quantity()`: Find extrema
- `normalize_units()`: Standardize units across quantities
- Quick functions: `convert_batch()`, `sum_batch()`

**Performance Profiling** (`unifyt.profiler`):
- `PerformanceProfiler` class for monitoring operations
- Context manager for profiling code blocks
- `@profile_function` decorator for function profiling
- Detailed statistics: count, total, mean, std, min, max, median
- Global profiler with `enable_profiling()` / `disable_profiling()`
- `print_profiling_stats()`: Display performance metrics
- Export statistics for analysis

**Metric Prefixes** (`unifyt.prefixes`):
- Auto-generate SI prefixed units (yotta to yocto)
- Binary prefixes (IEC): kibi, mebi, gibi, tebi, pebi, exbi
- `add_prefixes_to_unit()`: Add prefixes to custom units
- `add_binary_prefixes_to_unit()`: Add binary prefixes
- `generate_common_prefixed_units()`: Generate standard prefixed units
- `parse_prefixed_unit()`: Parse unit strings with prefixes
- Support for full names and symbols (e.g., 'kilometer' and 'km')

#### New Examples

- **v0.3.0_features.py**: Comprehensive showcase of all new features
  - Uncertain quantities with error propagation
  - All formatting styles demonstrated
  - Unit validation and suggestions
  - Batch operations and statistics
  - Performance profiling examples
  - Metric prefix generation
  - Real-world physics experiment example
  - Batch analysis of multiple experiments

### Changed

- Version bumped to 0.3.0
- Updated `__init__.py` to export new classes and functions
- Enhanced documentation with v0.3.0 features
- README updated with new feature highlights
- All new features maintain backward compatibility

### Performance

- Profiling tools allow users to identify bottlenecks
- Batch operations more efficient than individual conversions
- No performance degradation in existing features
- Unit caching still active for fast parsing

### Documentation

- New comprehensive example file showcasing all v0.3.0 features
- Updated README with feature highlights
- Inline documentation for all new classes and functions
- Type hints for better IDE support

### Developer Experience

- Better error messages with unit suggestions
- Validation before operations prevents runtime errors
- Profiling helps optimize user code
- Multiple formatting options for different output needs
- Uncertainty support for scientific applications

## [0.2.0] - 2024-12-24

### Added - Major Feature Release 🚀

#### Units (200+ new units added - now 300+ total!)

**Astronomical Units**:
- kiloparsec, megaparsec
- nautical_mile, fathom, chain, furlong, league
- picometer, femtometer, fermi

**Atomic & Nuclear**:
- atomic_mass_unit, dalton
- electron_mass, proton_mass, neutron_mass
- solar_mass, earth_mass
- carat, grain, stone, slug

**Advanced Time**:
- picosecond, femtosecond, attosecond
- shake, fortnight, month, decade, century, millennium

**Advanced Energy**:
- megajoule, gigajoule, erg
- british_thermal_unit, therm, quad
- ton_tnt, kiloton_tnt, megaton_tnt
- rydberg, hartree

**Advanced Power**:
- gigawatt, terawatt
- milliwatt, microwatt, nanowatt
- metric_horsepower, boiler_horsepower

**Advanced Pressure**:
- gigapascal, millibar, microbar, barye
- technical_atmosphere
- inch_mercury, millimeter_mercury

**Advanced Force**:
- meganewton, dyne
- kilogram_force, gram_force, ton_force
- poundal, kip

**Advanced Frequency**:
- terahertz, millihertz
- rpm (revolutions per minute)
- rps (revolutions per second)

**Advanced Voltage**:
- megavolt, microvolt, nanovolt
- statvolt

**Advanced Current**:
- microampere, nanoampere, picoampere
- kiloampere, statampere

**Capacitance**:
- farad, millifarad, microfarad, nanofarad, picofarad

**Inductance**:
- henry, millihenry, microhenry, nanohenry

**Magnetic Field**:
- tesla, millitesla, microtesla, nanotesla
- gauss, milligauss

**Magnetic Flux**:
- weber, milliweber, maxwell

**Illuminance**:
- lux, foot_candle, phot

**Luminous Flux**:
- lumen

**Radioactivity**:
- becquerel, kilobecquerel, megabecquerel, gigabecquerel
- curie, millicurie, microcurie
- rutherford

**Absorbed Dose**:
- gray, milligray, rad

**Equivalent Dose**:
- sievert, millisievert, microsievert
- rem, millirem

**Catalytic Activity**:
- katal, unit (enzyme unit)

**Data/Information**:
- bit, byte
- kilobyte, megabyte, gigabyte, terabyte, petabyte
- kibibyte, mebibyte, gibibyte, tebibyte

**Velocity**:
- knot, mach

**Acceleration**:
- gal (galileo), standard_gravity

**Viscosity**:
- pascal_second, poise, centipoise (dynamic)
- stokes, centistokes (kinematic)

**Thermal Properties**:
- watt_per_meter_kelvin (thermal conductivity)
- joule_per_kelvin (heat capacity)
- joule_per_kilogram_kelvin (specific heat)

**Molar Mass**:
- gram_per_mole, kilogram_per_mole

**Concentration**:
- molar, millimolar, micromolar, nanomolar

**Density**:
- kilogram_per_cubic_meter
- gram_per_cubic_centimeter
- gram_per_liter

**Flow Rate**:
- cubic_meter_per_second
- liter_per_second, liter_per_minute
- gallon_per_minute

**Fuel Efficiency**:
- mile_per_gallon, kilometer_per_liter
- liter_per_100km

**Angle**:
- arcminute, arcsecond, gradian

**Dimensionless**:
- ppt (parts per trillion)

#### Constants (50+ new constants added - now 80+ total!)

**Electromagnetic**:
- Faraday constant (F)
- Vacuum impedance (Z_0)
- Conductance quantum (G_0)
- Josephson constant (K_J)
- Von Klitzing constant (R_K)
- Magnetic flux quantum (Phi_0)
- Bohr magneton (mu_B)
- Nuclear magneton (mu_N)
- Proton/electron/neutron magnetic moments
- Proton gyromagnetic ratio

**Radiation**:
- Wien displacement constant
- First radiation constant
- Second radiation constant

**Atomic & Particle**:
- Compton wavelength
- Classical electron radius
- Thomson cross section
- Electron g-factor
- Muon mass
- Tau mass

**Planck Units**:
- Planck length (l_P)
- Planck mass (m_P)
- Planck time (t_P)
- Planck temperature (T_P)
- Planck energy (E_P)

**Cosmological**:
- Hubble constant (H_0)
- CMB temperature (T_CMB)
- Age of universe
- Critical density (rho_c)

**Solar System**:
- Solar luminosity (L_sun)
- Solar radius (R_sun)
- Jupiter mass (M_jupiter)
- Moon mass (M_moon)
- Schwarzschild radii (Earth, Sun)

### Changed
- Version bumped to 0.2.0
- Documentation updated across all files
- Examples updated with new units
- API reference expanded

### Performance
- No performance degradation
- Unit caching maintained
- Memory efficient despite 3x more units

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

[Unreleased]: https://github.com/MEERAN2314/unifyt/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.3.0
[0.2.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.2.0
[0.1.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.1.0
