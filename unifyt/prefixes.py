"""Automatic unit prefix generation (metric prefixes)."""

from typing import Dict, List, Tuple
from unifyt.unit_registry import UnitRegistry


# Standard SI prefixes
SI_PREFIXES: Dict[str, Tuple[str, float]] = {
    'yotta': ('Y', 1e24),
    'zetta': ('Z', 1e21),
    'exa': ('E', 1e18),
    'peta': ('P', 1e15),
    'tera': ('T', 1e12),
    'giga': ('G', 1e9),
    'mega': ('M', 1e6),
    'kilo': ('k', 1e3),
    'hecto': ('h', 1e2),
    'deca': ('da', 1e1),
    'deci': ('d', 1e-1),
    'centi': ('c', 1e-2),
    'milli': ('m', 1e-3),
    'micro': ('μ', 1e-6),
    'nano': ('n', 1e-9),
    'pico': ('p', 1e-12),
    'femto': ('f', 1e-15),
    'atto': ('a', 1e-18),
    'zepto': ('z', 1e-21),
    'yocto': ('y', 1e-24),
}

# Binary prefixes (IEC)
BINARY_PREFIXES: Dict[str, Tuple[str, float]] = {
    'kibi': ('Ki', 1024),
    'mebi': ('Mi', 1024**2),
    'gibi': ('Gi', 1024**3),
    'tebi': ('Ti', 1024**4),
    'pebi': ('Pi', 1024**5),
    'exbi': ('Ei', 1024**6),
}


def add_prefixes_to_unit(
    registry: UnitRegistry,
    base_unit: str,
    base_definition: str,
    prefixes: List[str] = None,
    exclude_prefixes: List[str] = None
) -> None:
    """
    Add metric prefixes to a base unit.
    
    Args:
        registry: UnitRegistry to add units to
        base_unit: Base unit name (e.g., 'meter')
        base_definition: Definition of base unit (e.g., '1 meter')
        prefixes: List of prefix names to add (default: all SI prefixes)
        exclude_prefixes: List of prefix names to exclude
    
    Examples:
        >>> registry = UnitRegistry()
        >>> add_prefixes_to_unit(registry, 'meter', '1 meter')
        >>> # Now registry has kilometer, centimeter, millimeter, etc.
    """
    if prefixes is None:
        prefixes = list(SI_PREFIXES.keys())
    
    if exclude_prefixes:
        prefixes = [p for p in prefixes if p not in exclude_prefixes]
    
    for prefix_name in prefixes:
        if prefix_name not in SI_PREFIXES:
            continue
        
        symbol, factor = SI_PREFIXES[prefix_name]
        
        # Full name (e.g., 'kilometer')
        full_name = f"{prefix_name}{base_unit}"
        definition = f"{factor} {base_definition}"
        registry.define(full_name, definition)
        
        # Symbol (e.g., 'km')
        if base_unit in ['meter', 'gram', 'second', 'liter']:
            base_symbol = {'meter': 'm', 'gram': 'g', 'second': 's', 'liter': 'L'}[base_unit]
            symbol_name = f"{symbol}{base_symbol}"
            registry.alias(symbol_name, full_name)


def add_binary_prefixes_to_unit(
    registry: UnitRegistry,
    base_unit: str,
    base_definition: str
) -> None:
    """
    Add binary (IEC) prefixes to a base unit.
    
    Args:
        registry: UnitRegistry to add units to
        base_unit: Base unit name (e.g., 'byte')
        base_definition: Definition of base unit (e.g., '8 bit')
    
    Examples:
        >>> registry = UnitRegistry()
        >>> add_binary_prefixes_to_unit(registry, 'byte', '8 bit')
        >>> # Now registry has kibibyte, mebibyte, gibibyte, etc.
    """
    for prefix_name, (symbol, factor) in BINARY_PREFIXES.items():
        full_name = f"{prefix_name}{base_unit}"
        definition = f"{factor} {base_definition}"
        registry.define(full_name, definition)
        
        # Symbol (e.g., 'KiB')
        if base_unit == 'byte':
            symbol_name = f"{symbol}B"
            registry.alias(symbol_name, full_name)


def generate_common_prefixed_units(registry: UnitRegistry) -> None:
    """
    Generate commonly used prefixed units.
    
    Args:
        registry: UnitRegistry to populate
    
    Examples:
        >>> registry = UnitRegistry()
        >>> generate_common_prefixed_units(registry)
    """
    # Length units
    add_prefixes_to_unit(
        registry, 'meter', '1 meter',
        prefixes=['kilo', 'centi', 'milli', 'micro', 'nano', 'pico']
    )
    
    # Mass units
    add_prefixes_to_unit(
        registry, 'gram', '0.001 kilogram',
        prefixes=['kilo', 'milli', 'micro']
    )
    
    # Time units
    add_prefixes_to_unit(
        registry, 'second', '1 second',
        prefixes=['milli', 'micro', 'nano', 'pico', 'femto']
    )
    
    # Volume units
    add_prefixes_to_unit(
        registry, 'liter', '0.001 meter^3',
        prefixes=['milli', 'micro']
    )
    
    # Data units
    add_binary_prefixes_to_unit(registry, 'byte', '8 bit')


def parse_prefixed_unit(unit_string: str) -> Tuple[str, float]:
    """
    Parse a unit string with prefix into base unit and scale factor.
    
    Args:
        unit_string: Unit string (e.g., 'kilometer', 'km')
    
    Returns:
        Tuple of (base_unit, scale_factor)
    
    Examples:
        >>> parse_prefixed_unit('kilometer')
        ('meter', 1000.0)
        >>> parse_prefixed_unit('millisecond')
        ('second', 0.001)
    """
    # Try full prefix names
    for prefix_name, (symbol, factor) in SI_PREFIXES.items():
        if unit_string.startswith(prefix_name):
            base = unit_string[len(prefix_name):]
            return (base, factor)
    
    # Try prefix symbols
    for prefix_name, (symbol, factor) in SI_PREFIXES.items():
        if unit_string.startswith(symbol):
            base = unit_string[len(symbol):]
            return (base, factor)
    
    # No prefix found
    return (unit_string, 1.0)
