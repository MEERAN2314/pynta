"""Unit validation and checking utilities."""

from typing import List, Tuple, Optional, Dict
from unifyt.unit import Unit
from unifyt.dimensions import Dimension
import re


class UnitValidator:
    """
    Validator for unit strings and operations.
    
    Examples:
        >>> validator = UnitValidator()
        >>> validator.is_valid('meter')  # True
        >>> validator.is_valid('invalid_unit')  # False
    """
    
    def __init__(self):
        """Initialize validator."""
        self._valid_units = set(Unit._CONVERSIONS.keys())
    
    def is_valid(self, unit_str: str) -> bool:
        """
        Check if a unit string is valid.
        
        Args:
            unit_str: Unit string to validate
        
        Returns:
            True if valid, False otherwise
        """
        try:
            Unit(unit_str)
            return True
        except Exception:
            return False
    
    def validate(self, unit_str: str) -> Tuple[bool, Optional[str]]:
        """
        Validate unit string and return error message if invalid.
        
        Args:
            unit_str: Unit string to validate
        
        Returns:
            Tuple of (is_valid, error_message)
        
        Examples:
            >>> validator = UnitValidator()
            >>> validator.validate('meter')
            (True, None)
            >>> validator.validate('invalid')
            (False, 'Unknown unit: invalid')
        """
        try:
            Unit(unit_str)
            return (True, None)
        except Exception as e:
            return (False, str(e))
    
    def suggest_corrections(self, unit_str: str, max_suggestions: int = 5) -> List[str]:
        """
        Suggest corrections for invalid unit strings.
        
        Args:
            unit_str: Invalid unit string
            max_suggestions: Maximum number of suggestions
        
        Returns:
            List of suggested corrections
        
        Examples:
            >>> validator = UnitValidator()
            >>> validator.suggest_corrections('metr')
            ['meter', 'meters']
        """
        suggestions = []
        unit_lower = unit_str.lower()
        
        # Find similar units using simple string matching
        for valid_unit in self._valid_units:
            if unit_lower in valid_unit.lower() or valid_unit.lower() in unit_lower:
                suggestions.append(valid_unit)
            elif self._levenshtein_distance(unit_lower, valid_unit.lower()) <= 2:
                suggestions.append(valid_unit)
        
        return suggestions[:max_suggestions]
    
    def check_dimensionality(
        self,
        unit1: str,
        unit2: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Check if two units have compatible dimensionality.
        
        Args:
            unit1: First unit string
            unit2: Second unit string
        
        Returns:
            Tuple of (is_compatible, error_message)
        
        Examples:
            >>> validator = UnitValidator()
            >>> validator.check_dimensionality('meter', 'foot')
            (True, None)
            >>> validator.check_dimensionality('meter', 'second')
            (False, 'Incompatible dimensions: ...')
        """
        try:
            u1 = Unit(unit1)
            u2 = Unit(unit2)
            
            if u1.is_compatible_with(u2):
                return (True, None)
            else:
                return (
                    False,
                    f"Incompatible dimensions: {unit1} has {u1.dimensionality}, "
                    f"{unit2} has {u2.dimensionality}"
                )
        except Exception as e:
            return (False, str(e))
    
    def parse_compound_unit(self, unit_str: str) -> Dict[str, float]:
        """
        Parse a compound unit into its components.
        
        Args:
            unit_str: Compound unit string (e.g., 'meter/second^2')
        
        Returns:
            Dictionary of {unit: power}
        
        Examples:
            >>> validator = UnitValidator()
            >>> validator.parse_compound_unit('meter/second^2')
            {'meter': 1.0, 'second': -2.0}
        """
        unit = Unit(unit_str)
        return unit._components
    
    def simplify_unit(self, unit_str: str) -> str:
        """
        Simplify a unit string by canceling common terms.
        
        Args:
            unit_str: Unit string to simplify
        
        Returns:
            Simplified unit string
        
        Examples:
            >>> validator = UnitValidator()
            >>> validator.simplify_unit('meter * second / second')
            'meter'
        """
        unit = Unit(unit_str)
        components = unit._components
        
        # Remove zero powers
        components = {u: p for u, p in components.items() if abs(p) > 1e-10}
        
        if not components:
            return 'dimensionless'
        
        # Build simplified string
        numerator = []
        denominator = []
        
        for unit_name, power in components.items():
            if power > 0:
                if abs(power - 1.0) < 1e-10:
                    numerator.append(unit_name)
                else:
                    numerator.append(f"{unit_name}^{power}")
            else:
                if abs(power + 1.0) < 1e-10:
                    denominator.append(unit_name)
                else:
                    denominator.append(f"{unit_name}^{abs(power)}")
        
        if not denominator:
            return ' * '.join(numerator)
        elif not numerator:
            return '1 / ' + ' * '.join(denominator)
        else:
            return ' * '.join(numerator) + ' / ' + ' * '.join(denominator)
    
    @staticmethod
    def _levenshtein_distance(s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return UnitValidator._levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                # Cost of insertions, deletions, or substitutions
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]


def validate_unit(unit_str: str) -> bool:
    """
    Quick validation function.
    
    Args:
        unit_str: Unit string to validate
    
    Returns:
        True if valid, False otherwise
    
    Examples:
        >>> validate_unit('meter')
        True
        >>> validate_unit('invalid')
        False
    """
    validator = UnitValidator()
    return validator.is_valid(unit_str)


def suggest_unit(unit_str: str) -> List[str]:
    """
    Quick suggestion function.
    
    Args:
        unit_str: Invalid unit string
    
    Returns:
        List of suggestions
    
    Examples:
        >>> suggest_unit('metr')
        ['meter', 'meters']
    """
    validator = UnitValidator()
    return validator.suggest_corrections(unit_str)
