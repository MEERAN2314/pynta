"""Advanced formatting options for quantities."""

from typing import Optional, Literal
from unifyt.quantity import Quantity
import numpy as np


FormatStyle = Literal['default', 'latex', 'unicode', 'html', 'compact', 'scientific']


class QuantityFormatter:
    """
    Advanced formatter for Quantity objects.
    
    Examples:
        >>> formatter = QuantityFormatter(style='latex')
        >>> q = Quantity(100, 'meter/second')
        >>> print(formatter.format(q))  # 100 \\frac{m}{s}
    """
    
    def __init__(
        self,
        style: FormatStyle = 'default',
        precision: int = 6,
        use_prefix: bool = True,
        compact: bool = False
    ):
        """
        Initialize formatter.
        
        Args:
            style: Output style (default, latex, unicode, html, compact, scientific)
            precision: Number of significant figures
            use_prefix: Use metric prefixes when possible
            compact: Use compact notation
        """
        self.style = style
        self.precision = precision
        self.use_prefix = use_prefix
        self.compact = compact
    
    def format(self, quantity: Quantity) -> str:
        """
        Format a quantity according to style.
        
        Args:
            quantity: Quantity to format
        
        Returns:
            Formatted string
        """
        if self.style == 'latex':
            return self._format_latex(quantity)
        elif self.style == 'unicode':
            return self._format_unicode(quantity)
        elif self.style == 'html':
            return self._format_html(quantity)
        elif self.style == 'compact':
            return self._format_compact(quantity)
        elif self.style == 'scientific':
            return self._format_scientific(quantity)
        else:
            return self._format_default(quantity)
    
    def _format_default(self, quantity: Quantity) -> str:
        """Default formatting."""
        value = quantity.magnitude
        unit = str(quantity.unit)
        
        if isinstance(value, np.ndarray):
            return f"{value} {unit}"
        
        return f"{value:.{self.precision}g} {unit}"
    
    def _format_latex(self, quantity: Quantity) -> str:
        """LaTeX formatting."""
        value = quantity.magnitude
        unit_str = str(quantity.unit)
        
        # Format value
        if isinstance(value, np.ndarray):
            val_str = str(value)
        else:
            val_str = f"{value:.{self.precision}g}"
        
        # Convert unit to LaTeX
        unit_latex = self._unit_to_latex(unit_str)
        
        return f"{val_str} {unit_latex}"
    
    def _format_unicode(self, quantity: Quantity) -> str:
        """Unicode formatting with superscripts/subscripts."""
        value = quantity.magnitude
        unit_str = str(quantity.unit)
        
        if isinstance(value, np.ndarray):
            val_str = str(value)
        else:
            val_str = f"{value:.{self.precision}g}"
        
        # Convert powers to unicode superscripts
        unit_unicode = self._unit_to_unicode(unit_str)
        
        return f"{val_str} {unit_unicode}"
    
    def _format_html(self, quantity: Quantity) -> str:
        """HTML formatting."""
        value = quantity.magnitude
        unit_str = str(quantity.unit)
        
        if isinstance(value, np.ndarray):
            val_str = str(value)
        else:
            val_str = f"{value:.{self.precision}g}"
        
        # Convert unit to HTML
        unit_html = self._unit_to_html(unit_str)
        
        return f"{val_str} {unit_html}"
    
    def _format_compact(self, quantity: Quantity) -> str:
        """Compact formatting."""
        value = quantity.magnitude
        unit_str = str(quantity.unit)
        
        if isinstance(value, np.ndarray):
            return f"{value}{unit_str}"
        
        return f"{value:.{self.precision}g}{unit_str}"
    
    def _format_scientific(self, quantity: Quantity) -> str:
        """Scientific notation formatting."""
        value = quantity.magnitude
        unit_str = str(quantity.unit)
        
        if isinstance(value, np.ndarray):
            val_str = str(value)
        else:
            val_str = f"{value:.{self.precision}e}"
        
        return f"{val_str} {unit_str}"
    
    def _unit_to_latex(self, unit_str: str) -> str:
        """Convert unit string to LaTeX."""
        # Handle division
        if '/' in unit_str:
            parts = unit_str.split('/')
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            return f"\\frac{{{numerator}}}{{{denominator}}}"
        
        # Handle powers
        unit_str = unit_str.replace('^', '^{')
        if '^{' in unit_str:
            unit_str = unit_str.replace(' ', '} ')
            if not unit_str.endswith('}'):
                unit_str += '}'
        
        return f"\\mathrm{{{unit_str}}}"
    
    def _unit_to_unicode(self, unit_str: str) -> str:
        """Convert unit string to unicode with superscripts."""
        # Unicode superscript mapping
        superscripts = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
            '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
            '-': '⁻', '+': '⁺'
        }
        
        result = unit_str
        # Replace ^X with superscript
        i = 0
        while i < len(result):
            if result[i] == '^':
                # Find the number after ^
                j = i + 1
                while j < len(result) and (result[j].isdigit() or result[j] in '-+'):
                    j += 1
                
                # Convert to superscript
                power = result[i+1:j]
                superscript = ''.join(superscripts.get(c, c) for c in power)
                result = result[:i] + superscript + result[j:]
                i = i + len(superscript)
            else:
                i += 1
        
        return result
    
    def _unit_to_html(self, unit_str: str) -> str:
        """Convert unit string to HTML."""
        # Handle division
        if '/' in unit_str:
            parts = unit_str.split('/')
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            return f"{numerator}/{denominator}"
        
        # Handle powers
        result = unit_str
        i = 0
        while i < len(result):
            if result[i] == '^':
                # Find the number after ^
                j = i + 1
                while j < len(result) and (result[j].isdigit() or result[j] in '-+'):
                    j += 1
                
                power = result[i+1:j]
                result = result[:i] + f"<sup>{power}</sup>" + result[j:]
                i = i + len(f"<sup>{power}</sup>")
            else:
                i += 1
        
        return result


def format_quantity(
    quantity: Quantity,
    style: FormatStyle = 'default',
    precision: int = 6
) -> str:
    """
    Quick format function.
    
    Args:
        quantity: Quantity to format
        style: Output style
        precision: Number of significant figures
    
    Returns:
        Formatted string
    
    Examples:
        >>> q = Quantity(100, 'meter/second')
        >>> format_quantity(q, style='latex')
        '100 \\frac{meter}{second}'
    """
    formatter = QuantityFormatter(style=style, precision=precision)
    return formatter.format(quantity)
