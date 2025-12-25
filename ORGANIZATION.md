# Unifyt Project Organization

This document explains how the Unifyt project is organized and maintained.

## Quick Navigation

| Need | File |
|------|------|
| **Start using Unifyt** | [GETTING_STARTED.md](GETTING_STARTED.md) |
| **5-minute intro** | [QUICKSTART.md](QUICKSTART.md) |
| **Find anything** | [INDEX.md](INDEX.md) |
| **Project structure** | [STRUCTURE.md](STRUCTURE.md) |
| **What's included** | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
| **What was improved** | [IMPROVEMENTS_SUMMARY.md](IMPROVEMENTS_SUMMARY.md) |

## File Organization

### 📋 Documentation Hierarchy

```
Root Documentation (Start Here)
├── README.md                    # Project overview
├── INDEX.md                     # Complete navigation
├── GETTING_STARTED.md           # Comprehensive tutorial
├── QUICKSTART.md                # 5-minute intro
└── ORGANIZATION.md              # This file

Project Information
├── STRUCTURE.md                 # Project structure
├── PROJECT_SUMMARY.md           # Complete summary
├── IMPROVEMENTS_SUMMARY.md      # What was improved
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # How to contribute
└── LICENSE                      # MIT License

Technical Documentation (docs/)
├── user_guide.md                # Complete usage guide
├── api_reference.md             # Full API docs
├── FEATURES.md                  # Feature list
├── PERFORMANCE.md               # Performance guide
└── MIGRATION.md                 # Migration guide
```

### 🎯 Reading Order for New Users

1. **README.md** - Get an overview
2. **GETTING_STARTED.md** - Learn the basics
3. **examples/basic_usage.py** - See it in action
4. **docs/user_guide.md** - Deep dive
5. **examples/** - Explore more examples

### 🔧 Reading Order for Developers

1. **STRUCTURE.md** - Understand the layout
2. **CONTRIBUTING.md** - Learn how to contribute
3. **PROJECT_SUMMARY.md** - See the big picture
4. **tests/** - Study the tests
5. **unifyt/** - Read the source code

## Code Organization

### Module Responsibilities

| Module | Responsibility | Dependencies |
|--------|---------------|--------------|
| `quantity.py` | Core Quantity class | unit, dimensions, numpy |
| `unit.py` | Unit definitions & conversions | dimensions |
| `dimensions.py` | Physical dimensions | None |
| `constants.py` | Physical constants | quantity |
| `utils.py` | Utility functions | quantity, numpy |
| `serialization.py` | JSON/pickle support | quantity, unit |
| `unit_registry.py` | Custom units | unit |
| `context.py` | Unit system contexts | None |

### Import Structure

```python
# Clean import hierarchy
unifyt/
  __init__.py          # Exports main API
    ├── quantity       # Core class
    ├── unit           # Unit class
    ├── dimensions     # Dimension class
    ├── constants      # Constants module
    ├── utils          # Utilities module
    └── serialization  # Serialization functions
```

### Circular Dependency Prevention

- `dimensions.py` has no dependencies
- `unit.py` only depends on `dimensions.py`
- `quantity.py` depends on `unit.py` and `dimensions.py`
- `constants.py` depends on `quantity.py`
- `utils.py` depends on `quantity.py`

## Testing Organization

### Test Structure

```
tests/
├── conftest.py              # Shared fixtures
├── test_dimensions.py       # Dimension tests
├── test_unit.py             # Unit tests
├── test_quantity.py         # Quantity tests
├── test_unit_registry.py    # Registry tests
├── test_context.py          # Context tests
├── test_constants.py        # Constants tests
├── test_utils.py            # Utility tests
└── test_serialization.py    # Serialization tests
```

### Test Coverage

- **Unit tests**: Test individual functions/methods
- **Integration tests**: Test module interactions
- **Edge cases**: Test boundary conditions
- **Array tests**: Test NumPy integration

## Example Organization

### Example Progression

1. **basic_usage.py** - Fundamentals
2. **scientific_calculations.py** - Real applications
3. **custom_units.py** - Customization
4. **array_operations.py** - Data handling
5. **advanced_features.py** - Advanced topics
6. **complete_demo.py** - Everything together

## Documentation Organization

### Documentation Types

| Type | Files | Purpose |
|------|-------|---------|
| **Getting Started** | GETTING_STARTED.md, QUICKSTART.md | New user onboarding |
| **Reference** | docs/api_reference.md | Complete API docs |
| **Guides** | docs/user_guide.md | How-to guides |
| **Explanations** | docs/FEATURES.md, docs/PERFORMANCE.md | Deep dives |
| **Project Info** | PROJECT_SUMMARY.md, STRUCTURE.md | Project overview |

### Documentation Standards

- **Markdown format** for all docs
- **Code examples** in all guides
- **Clear headings** for navigation
- **Cross-references** between docs
- **Up-to-date** with code

## Development Workflow

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/unifyt.git
cd unifyt

# Set up development environment
make install-dev
# or
./setup_dev.sh
```

### Development Cycle

```bash
# 1. Make changes to code
vim unifyt/quantity.py

# 2. Format code
make format

# 3. Run linters
make lint

# 4. Run tests
make test

# 5. Run examples
make examples

# 6. Validate project
make validate
```

### Before Committing

```bash
# Run all checks
make all

# Or manually:
make format    # Format code
make lint      # Check code quality
make test      # Run tests
```

## Maintenance Tasks

### Regular Maintenance

```bash
# Clean temporary files
make clean

# Update dependencies
pip install --upgrade -r requirements-dev.txt

# Run full validation
make validate
```

### Release Checklist

1. Update version in `setup.py` and `unifyt/__init__.py`
2. Update `CHANGELOG.md`
3. Run `make all` to verify everything works
4. Create git tag
5. Build distribution: `python setup.py sdist bdist_wheel`
6. Upload to PyPI: `twine upload dist/*`

## File Naming Conventions

### Python Files
- **Lowercase with underscores**: `unit_registry.py`
- **Test prefix**: `test_quantity.py`
- **Example suffix**: `basic_usage.py`

### Documentation Files
- **UPPERCASE for root docs**: `README.md`, `CONTRIBUTING.md`
- **Lowercase for guides**: `user_guide.md`
- **UPPERCASE for special**: `FEATURES.md`, `PERFORMANCE.md`

### Scripts
- **Lowercase with underscores**: `run_tests.sh`
- **Descriptive names**: `setup_dev.sh`, `check_code.sh`

## Code Style

### Python Style
- **PEP 8** compliant
- **Black** formatted (line length: 100)
- **Type hints** for all public APIs
- **Docstrings** for all public functions/classes

### Documentation Style
- **Markdown** for all docs
- **Code blocks** with language tags
- **Clear examples** for all features
- **Cross-references** using relative links

## Quality Standards

### Code Quality
- ✅ Type hints on all public APIs
- ✅ Docstrings on all public functions
- ✅ PEP 8 compliant
- ✅ Black formatted
- ✅ Mypy type checked
- ✅ Flake8 linted

### Test Quality
- ✅ >90% code coverage
- ✅ All features tested
- ✅ Edge cases covered
- ✅ Integration tests included

### Documentation Quality
- ✅ Complete API reference
- ✅ User guide with examples
- ✅ Getting started guide
- ✅ Performance guide
- ✅ Migration guide

## Tools and Scripts

### Available Commands

| Command | Purpose |
|---------|---------|
| `make install` | Install package |
| `make install-dev` | Install with dev dependencies |
| `make test` | Run tests |
| `make test-cov` | Run tests with coverage |
| `make clean` | Remove temporary files |
| `make format` | Format code |
| `make lint` | Run linters |
| `make check` | Run all checks |
| `make examples` | Run all examples |
| `make validate` | Validate project |
| `make all` | Format, lint, and test |

### Shell Scripts

| Script | Purpose |
|--------|---------|
| `setup_dev.sh` | Set up development environment |
| `run_tests.sh` | Run test suite |
| `run_examples.sh` | Run all examples |
| `check_code.sh` | Check code quality |
| `format_code.sh` | Format code |
| `clean.sh` | Clean temporary files |
| `validate.sh` | Validate project structure |

## Best Practices

### When Adding Features

1. **Write tests first** (TDD)
2. **Update documentation**
3. **Add examples** if applicable
4. **Run all checks** before committing
5. **Update CHANGELOG.md**

### When Fixing Bugs

1. **Write a failing test** that reproduces the bug
2. **Fix the bug**
3. **Verify the test passes**
4. **Update documentation** if needed
5. **Add to CHANGELOG.md**

### When Writing Documentation

1. **Start with examples**
2. **Explain the why**, not just the how
3. **Cross-reference** related docs
4. **Keep it up-to-date** with code
5. **Test all code examples**

## Project Health Indicators

### Good Signs ✅
- All tests passing
- High code coverage (>90%)
- No linter warnings
- Documentation up-to-date
- Examples all work
- Clean git history

### Warning Signs ⚠️
- Failing tests
- Low code coverage (<80%)
- Linter warnings
- Outdated documentation
- Broken examples
- Messy commits

## Getting Help

### For Users
1. Check [INDEX.md](INDEX.md) for navigation
2. Read [GETTING_STARTED.md](GETTING_STARTED.md)
3. Browse [examples/](examples/)
4. Read [docs/user_guide.md](docs/user_guide.md)
5. Open a GitHub issue

### For Contributors
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Check [STRUCTURE.md](STRUCTURE.md)
3. Study the tests
4. Ask questions in issues
5. Submit a pull request

## Summary

The Unifyt project is organized for:
- **Easy navigation** - Clear file structure
- **Quick onboarding** - Progressive documentation
- **High quality** - Comprehensive testing
- **Easy maintenance** - Automated tools
- **Clear standards** - Consistent style

Everything has its place, and there's a place for everything! 🎯
