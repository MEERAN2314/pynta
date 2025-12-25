"""Unit class for representing physical units."""

from __future__ import annotations
from typing import Dict, Optional
from unifyt.dimensions import Dimension


class Unit:
    """
    Represents a physical unit.
    
    Examples:
        >>> meter = Unit('meter')
        >>> second = Unit('second')
        >>> speed_unit = meter / second
    """
    
    # Base SI units
    _BASE_UNITS = {
        'meter': Dimension(length=1),
        'kilogram': Dimension(mass=1),
        'second': Dimension(time=1),
        'ampere': Dimension(current=1),
        'kelvin': Dimension(temperature=1),
        'mole': Dimension(amount=1),
        'candela': Dimension(luminosity=1),
        'dimensionless': Dimension(),
    }
    
    # Conversion factors to base units
    _CONVERSIONS = {
        # Length
        'meter': 1.0, 'm': 1.0, 'meters': 1.0,
        'kilometer': 1000.0, 'km': 1000.0, 'kilometers': 1000.0,
        'centimeter': 0.01, 'cm': 0.01, 'centimeters': 0.01,
        'millimeter': 0.001, 'mm': 0.001, 'millimeters': 0.001,
        'micrometer': 1e-6, 'um': 1e-6, 'micrometers': 1e-6,
        'nanometer': 1e-9, 'nm': 1e-9, 'nanometers': 1e-9,
        'angstrom': 1e-10, 'Å': 1e-10,
        'mile': 1609.344, 'mi': 1609.344, 'miles': 1609.344,
        'yard': 0.9144, 'yd': 0.9144, 'yards': 0.9144,
        'foot': 0.3048, 'ft': 0.3048, 'feet': 0.3048,
        'inch': 0.0254, 'in': 0.0254, 'inches': 0.0254,
        
        # Mass
        'kilogram': 1.0, 'kg': 1.0, 'kilograms': 1.0,
        'gram': 0.001, 'g': 0.001, 'grams': 0.001,
        'milligram': 1e-6, 'mg': 1e-6, 'milligrams': 1e-6,
        'microgram': 1e-9, 'ug': 1e-9, 'micrograms': 1e-9,
        'pound': 0.453592, 'lb': 0.453592, 'pounds': 0.453592,
        'ounce': 0.0283495, 'oz': 0.0283495, 'ounces': 0.0283495,
        'ton': 1000.0, 'tons': 1000.0, 'tonne': 1000.0, 'tonnes': 1000.0,
        
        # Time
        'second': 1.0, 's': 1.0, 'seconds': 1.0, 'sec': 1.0,
        'millisecond': 0.001, 'ms': 0.001, 'milliseconds': 0.001,
        'microsecond': 1e-6, 'us': 1e-6, 'microseconds': 1e-6,
        'nanosecond': 1e-9, 'ns': 1e-9, 'nanoseconds': 1e-9,
        'minute': 60.0, 'min': 60.0, 'minutes': 60.0,
        'hour': 3600.0, 'h': 3600.0, 'hr': 3600.0, 'hours': 3600.0,
        'day': 86400.0, 'd': 86400.0, 'days': 86400.0,
        'week': 604800.0, 'weeks': 604800.0,
        'year': 31536000.0, 'yr': 31536000.0, 'years': 31536000.0,
        
        # Temperature (offset handled separately)
        'kelvin': 1.0, 'K': 1.0,
        'celsius': 1.0, 'C': 1.0, 'degC': 1.0,
        'fahrenheit': 5.0/9.0, 'F': 5.0/9.0, 'degF': 5.0/9.0,
        
        # Current
        'ampere': 1.0, 'A': 1.0, 'amperes': 1.0, 'amp': 1.0, 'amps': 1.0,
        'milliampere': 0.001, 'mA': 0.001,
        
        # Amount
        'mole': 1.0, 'mol': 1.0, 'moles': 1.0,
        
        # Luminosity
        'candela': 1.0, 'cd': 1.0,
        
        # Energy
        'joule': 1.0, 'J': 1.0, 'joules': 1.0,
        'kilojoule': 1000.0, 'kJ': 1000.0,
        'calorie': 4.184, 'cal': 4.184, 'calories': 4.184,
        'kilocalorie': 4184.0, 'kcal': 4184.0, 'Calorie': 4184.0,
        'electronvolt': 1.602176634e-19, 'eV': 1.602176634e-19,
        'watt_hour': 3600.0, 'Wh': 3600.0,
        'kilowatt_hour': 3.6e6, 'kWh': 3.6e6,
        
        # Power
        'watt': 1.0, 'W': 1.0, 'watts': 1.0,
        'kilowatt': 1000.0, 'kW': 1000.0, 'kilowatts': 1000.0,
        'megawatt': 1e6, 'MW': 1e6, 'megawatts': 1e6,
        'horsepower': 745.7, 'hp': 745.7,
        
        # Pressure
        'pascal': 1.0, 'Pa': 1.0,
        'kilopascal': 1000.0, 'kPa': 1000.0,
        'megapascal': 1e6, 'MPa': 1e6,
        'bar': 1e5, 'bars': 1e5,
        'atmosphere': 101325.0, 'atm': 101325.0,
        'psi': 6894.76, 'PSI': 6894.76,
        'torr': 133.322, 'Torr': 133.322,
        
        # Force
        'newton': 1.0, 'N': 1.0, 'newtons': 1.0,
        'kilonewton': 1000.0, 'kN': 1000.0,
        'pound_force': 4.44822, 'lbf': 4.44822,
        
        # Frequency
        'hertz': 1.0, 'Hz': 1.0,
        'kilohertz': 1000.0, 'kHz': 1000.0,
        'megahertz': 1e6, 'MHz': 1e6,
        'gigahertz': 1e9, 'GHz': 1e9,
        
        # Voltage
        'volt': 1.0, 'V': 1.0, 'volts': 1.0,
        'millivolt': 0.001, 'mV': 0.001,
        'kilovolt': 1000.0, 'kV': 1000.0,
        
        # Charge
        'coulomb': 1.0, 'C': 1.0, 'coulombs': 1.0,
        
        # Resistance
        'ohm': 1.0, 'Ω': 1.0, 'ohms': 1.0,
        'kiloohm': 1000.0, 'kΩ': 1000.0,
        'megaohm': 1e6, 'MΩ': 1e6,
        
        # Volume
        'liter': 0.001, 'L': 0.001, 'liters': 0.001, 'litre': 0.001, 'litres': 0.001,
        'milliliter': 1e-6, 'mL': 1e-6, 'milliliters': 1e-6,
        'gallon': 0.00378541, 'gal': 0.00378541, 'gallons': 0.00378541,
        'quart': 0.000946353, 'qt': 0.000946353,
        'pint': 0.000473176, 'pt': 0.000473176,
        'cup': 0.000236588, 'cups': 0.000236588,
        'fluid_ounce': 2.95735e-5, 'fl_oz': 2.95735e-5,
        
        # Area (derived but commonly used)
        'hectare': 10000.0, 'ha': 10000.0,
        'acre': 4046.86, 'acres': 4046.86,
        
        # Angle
        'radian': 1.0, 'rad': 1.0, 'radians': 1.0,
        'degree': 0.0174533, 'deg': 0.0174533, 'degrees': 0.0174533,
        
        # Dimensionless
        'dimensionless': 1.0,
        'percent': 0.01, '%': 0.01,
        'ppm': 1e-6,
        'ppb': 1e-9,
    }
    
    # Map units to their base unit (auto-generated from conversions)
    _UNIT_TO_BASE = None  # Will be generated dynamically
    
    # Temperature offset units (special handling)
    _TEMPERATURE_OFFSETS = {
        'celsius': 273.15,
        'C': 273.15,
        'degC': 273.15,
        'fahrenheit': 459.67,
        'F': 459.67,
        'degF': 459.67,
    }
    
    # Cache for parsed units
    _unit_cache: Dict[str, 'Unit'] = {}
    
    @classmethod
    def _build_unit_to_base_map(cls) -> Dict[str, str]:
        """Build the unit to base unit mapping."""
        if cls._UNIT_TO_BASE is not None:
            return cls._UNIT_TO_BASE
        
        mapping = {}
        # Length units
        length_units = ['meter', 'm', 'meters', 'kilometer', 'km', 'kilometers', 
                       'centimeter', 'cm', 'centimeters', 'millimeter', 'mm', 'millimeters',
                       'micrometer', 'um', 'micrometers', 'nanometer', 'nm', 'nanometers',
                       'angstrom', 'Å', 'mile', 'mi', 'miles', 'yard', 'yd', 'yards',
                       'foot', 'ft', 'feet', 'inch', 'in', 'inches']
        for u in length_units:
            mapping[u] = 'meter'
        
        # Mass units
        mass_units = ['kilogram', 'kg', 'kilograms', 'gram', 'g', 'grams',
                     'milligram', 'mg', 'milligrams', 'microgram', 'ug', 'micrograms',
                     'pound', 'lb', 'pounds', 'ounce', 'oz', 'ounces',
                     'ton', 'tons', 'tonne', 'tonnes']
        for u in mass_units:
            mapping[u] = 'kilogram'
        
        # Time units
        time_units = ['second', 's', 'seconds', 'sec', 'millisecond', 'ms', 'milliseconds',
                     'microsecond', 'us', 'microseconds', 'nanosecond', 'ns', 'nanoseconds',
                     'minute', 'min', 'minutes', 'hour', 'h', 'hr', 'hours',
                     'day', 'd', 'days', 'week', 'weeks', 'year', 'yr', 'years']
        for u in time_units:
            mapping[u] = 'second'
        
        # Temperature units
        temp_units = ['kelvin', 'K', 'celsius', 'C', 'degC', 'fahrenheit', 'F', 'degF']
        for u in temp_units:
            mapping[u] = 'kelvin'
        
        # Current units
        current_units = ['ampere', 'A', 'amperes', 'amp', 'amps', 'milliampere', 'mA']
        for u in current_units:
            mapping[u] = 'ampere'
        
        # Amount units
        amount_units = ['mole', 'mol', 'moles']
        for u in amount_units:
            mapping[u] = 'mole'
        
        # Luminosity units
        lum_units = ['candela', 'cd']
        for u in lum_units:
            mapping[u] = 'candela'
        
        # Dimensionless
        mapping['dimensionless'] = 'dimensionless'
        mapping['percent'] = 'dimensionless'
        mapping['%'] = 'dimensionless'
        mapping['ppm'] = 'dimensionless'
        mapping['ppb'] = 'dimensionless'
        
        cls._UNIT_TO_BASE = mapping
        return mapping
    
    def __init__(self, unit_str: str, scale: float = 1.0):
        """
        Initialize a Unit.
        
        Args:
            unit_str: String representation of the unit
            scale: Scale factor for the unit
        """
        # Check cache first
        cache_key = f"{unit_str}:{scale}"
        if cache_key in Unit._unit_cache:
            cached = Unit._unit_cache[cache_key]
            self._name = cached._name
            self._components = cached._components
            self._scale = cached._scale
            return
        
        self._parse_unit(unit_str)
        self._scale = scale
        
        # Cache the unit
        if len(Unit._unit_cache) < 1000:  # Limit cache size
            Unit._unit_cache[cache_key] = self
    
    def _parse_unit(self, unit_str: str) -> None:
        """Parse unit string into components."""
        # Simple parsing - handle basic units and compound units
        if '/' in unit_str:
            parts = unit_str.split('/')
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            
            num_unit = Unit(numerator)
            den_unit = Unit(denominator)
            
            self._components = num_unit._components.copy()
            for unit, power in den_unit._components.items():
                self._components[unit] = self._components.get(unit, 0) - power
            self._name = unit_str
        elif '*' in unit_str or ' ' in unit_str:
            # Handle multiplication
            separator = '*' if '*' in unit_str else ' '
            parts = [p.strip() for p in unit_str.split(separator) if p.strip()]
            
            self._components: Dict[str, float] = {}
            for part in parts:
                unit = Unit(part)
                for u, p in unit._components.items():
                    self._components[u] = self._components.get(u, 0) + p
            self._name = unit_str
        else:
            # Single unit
            self._name = unit_str.strip()
            self._components = {self._name: 1.0}
    
    @property
    def dimensionality(self) -> Dimension:
        """Get the dimensionality of this unit."""
        # Build mapping if not done yet
        unit_to_base = self._build_unit_to_base_map()
        
        dim = Dimension()
        for unit, power in self._components.items():
            base_unit = unit_to_base.get(unit, unit)
            if base_unit in self._BASE_UNITS:
                base_dim = self._BASE_UNITS[base_unit]
                dim = dim + (base_dim * power)
        return dim
    
    def is_compatible_with(self, other: Unit) -> bool:
        """Check if this unit is compatible with another."""
        return self.dimensionality == other.dimensionality
    
    def conversion_factor_to(self, other: Unit) -> float:
        """Get conversion factor to another unit."""
        if not self.is_compatible_with(other):
            raise ValueError(f"Incompatible units: {self} and {other}")
        
        # Calculate conversion factor
        self_factor = 1.0
        for unit, power in self._components.items():
            self_factor *= self._CONVERSIONS.get(unit, 1.0) ** power
        
        other_factor = 1.0
        for unit, power in other._components.items():
            other_factor *= other._CONVERSIONS.get(unit, 1.0) ** power
        
        return self_factor / other_factor * self._scale / other._scale
    
    def to_base_units(self) -> Unit:
        """Convert to base SI units."""
        unit_to_base = self._build_unit_to_base_map()
        
        base_components: Dict[str, float] = {}
        for unit, power in self._components.items():
            base_unit = unit_to_base.get(unit, unit)
            base_components[base_unit] = base_components.get(base_unit, 0) + power
        
        # Build base unit string
        numerator = []
        denominator = []
        for unit, power in base_components.items():
            if power > 0:
                if power == 1:
                    numerator.append(unit)
                else:
                    numerator.append(f"{unit}^{power}")
            elif power < 0:
                if power == -1:
                    denominator.append(unit)
                else:
                    denominator.append(f"{unit}^{-power}")
        
        if not numerator and not denominator:
            return Unit("dimensionless")
        elif not denominator:
            return Unit(" * ".join(numerator))
        elif not numerator:
            return Unit("1 / " + " * ".join(denominator))
        else:
            return Unit(" * ".join(numerator) + " / " + " * ".join(denominator))
    
    def is_dimensionless(self) -> bool:
        """Check if unit is dimensionless."""
        return self.dimensionality == Dimension()
    
    def __mul__(self, other: Unit) -> Unit:
        """Multiply units."""
        new_components = self._components.copy()
        for unit, power in other._components.items():
            new_components[unit] = new_components.get(unit, 0) + power
        
        # Build new unit string
        parts = []
        for unit, power in new_components.items():
            if power != 0:
                if power == 1:
                    parts.append(unit)
                else:
                    parts.append(f"{unit}^{power}")
        
        unit_str = " * ".join(parts) if parts else "dimensionless"
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale * other._scale
        return result
    
    def __truediv__(self, other: Unit) -> Unit:
        """Divide units."""
        new_components = self._components.copy()
        for unit, power in other._components.items():
            new_components[unit] = new_components.get(unit, 0) - power
        
        # Build new unit string
        numerator = []
        denominator = []
        for unit, power in new_components.items():
            if power > 0:
                if power == 1:
                    numerator.append(unit)
                else:
                    numerator.append(f"{unit}^{power}")
            elif power < 0:
                if power == -1:
                    denominator.append(unit)
                else:
                    denominator.append(f"{unit}^{abs(power)}")
        
        if not numerator and not denominator:
            unit_str = "dimensionless"
        elif not denominator:
            unit_str = " * ".join(numerator)
        elif not numerator:
            unit_str = "1 / " + " * ".join(denominator)
        else:
            unit_str = " * ".join(numerator) + " / " + " * ".join(denominator)
        
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale / other._scale
        return result
    
    def __pow__(self, exponent: float) -> Unit:
        """Raise unit to a power."""
        new_components = {unit: power * exponent for unit, power in self._components.items()}
        
        parts = []
        for unit, power in new_components.items():
            if power == 1:
                parts.append(unit)
            else:
                parts.append(f"{unit}^{power}")
        
        unit_str = " * ".join(parts) if parts else "dimensionless"
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale ** exponent
        return result
    
    def __eq__(self, other: object) -> bool:
        """Check equality."""
        if not isinstance(other, Unit):
            return False
        return self._components == other._components
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Unit('{self._name}')"
    
    def __str__(self) -> str:
        """Human-readable string."""
        return self._name
