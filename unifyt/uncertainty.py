"""Support for quantities with uncertainties."""

from __future__ import annotations
from typing import Union, Optional
import numpy as np
from unifyt.quantity import Quantity
from unifyt.unit import Unit


class UncertainQuantity(Quantity):
    """
    Quantity with uncertainty/error margin.
    
    Examples:
        >>> measurement = UncertainQuantity(100, 'meter', uncertainty=0.5)
        >>> print(measurement)  # 100.0 ± 0.5 meter
        >>> result = measurement * 2
        >>> print(result)  # 200.0 ± 1.0 meter
    """
    
    def __init__(
        self,
        value: Union[float, int, np.ndarray],
        unit: Union[str, Unit],
        uncertainty: Optional[Union[float, np.ndarray]] = None,
        relative_uncertainty: Optional[float] = None
    ):
        """
        Initialize an uncertain quantity.
        
        Args:
            value: Numerical value
            unit: Unit as string or Unit object
            uncertainty: Absolute uncertainty (same units as value)
            relative_uncertainty: Relative uncertainty (fraction)
        """
        super().__init__(value, unit)
        
        if uncertainty is not None:
            self._uncertainty = np.asarray(uncertainty)
        elif relative_uncertainty is not None:
            self._uncertainty = np.abs(self._value) * relative_uncertainty
        else:
            self._uncertainty = np.zeros_like(self._value)
    
    @property
    def uncertainty(self) -> np.ndarray:
        """Get the absolute uncertainty."""
        return self._uncertainty
    
    @property
    def relative_uncertainty(self) -> np.ndarray:
        """Get the relative uncertainty."""
        with np.errstate(divide='ignore', invalid='ignore'):
            rel = self._uncertainty / np.abs(self._value)
            # Handle both scalar and array cases
            if np.isscalar(rel) or rel.shape == ():
                if not np.isfinite(rel):
                    rel = np.array(0.0)
            else:
                rel[~np.isfinite(rel)] = 0
        return rel
    
    @property
    def std_dev(self) -> np.ndarray:
        """Alias for uncertainty (standard deviation)."""
        return self._uncertainty
    
    def to(self, target_unit: Union[str, Unit]) -> UncertainQuantity:
        """Convert to different unit, preserving uncertainty."""
        converted = super().to(target_unit)
        target = Unit(target_unit) if isinstance(target_unit, str) else target_unit
        conversion_factor = self._unit.conversion_factor_to(target)
        new_uncertainty = self._uncertainty * conversion_factor
        
        return UncertainQuantity(
            converted.value,
            converted.unit,
            uncertainty=new_uncertainty
        )
    
    def __add__(self, other: Union[UncertainQuantity, Quantity, float, int]) -> UncertainQuantity:
        """Add with uncertainty propagation."""
        result = super().__add__(other)
        
        if isinstance(other, UncertainQuantity):
            other_converted = other.to(self._unit)
            # Uncertainty propagation: σ_sum = sqrt(σ_a² + σ_b²)
            new_uncertainty = np.sqrt(
                self._uncertainty**2 + other_converted._uncertainty**2
            )
        elif isinstance(other, Quantity):
            new_uncertainty = self._uncertainty
        else:
            new_uncertainty = self._uncertainty
        
        return UncertainQuantity(result.value, result.unit, uncertainty=new_uncertainty)
    
    def __sub__(self, other: Union[UncertainQuantity, Quantity, float, int]) -> UncertainQuantity:
        """Subtract with uncertainty propagation."""
        result = super().__sub__(other)
        
        if isinstance(other, UncertainQuantity):
            other_converted = other.to(self._unit)
            # Same as addition for independent variables
            new_uncertainty = np.sqrt(
                self._uncertainty**2 + other_converted._uncertainty**2
            )
        elif isinstance(other, Quantity):
            new_uncertainty = self._uncertainty
        else:
            new_uncertainty = self._uncertainty
        
        return UncertainQuantity(result.value, result.unit, uncertainty=new_uncertainty)
    
    def __mul__(self, other: Union[UncertainQuantity, Quantity, float, int]) -> UncertainQuantity:
        """Multiply with uncertainty propagation."""
        result = super().__mul__(other)
        
        if isinstance(other, UncertainQuantity):
            # Relative uncertainty propagation: σ_rel = sqrt((σ_a/a)² + (σ_b/b)²)
            rel_unc_self = self.relative_uncertainty
            rel_unc_other = other.relative_uncertainty
            rel_unc_result = np.sqrt(rel_unc_self**2 + rel_unc_other**2)
            new_uncertainty = np.abs(result.value) * rel_unc_result
        elif isinstance(other, Quantity):
            new_uncertainty = self._uncertainty * np.abs(other.value)
        else:
            new_uncertainty = self._uncertainty * np.abs(other)
        
        return UncertainQuantity(result.value, result.unit, uncertainty=new_uncertainty)
    
    def __truediv__(self, other: Union[UncertainQuantity, Quantity, float, int]) -> UncertainQuantity:
        """Divide with uncertainty propagation."""
        result = super().__truediv__(other)
        
        if isinstance(other, UncertainQuantity):
            # Same relative uncertainty formula as multiplication
            rel_unc_self = self.relative_uncertainty
            rel_unc_other = other.relative_uncertainty
            rel_unc_result = np.sqrt(rel_unc_self**2 + rel_unc_other**2)
            new_uncertainty = np.abs(result.value) * rel_unc_result
        elif isinstance(other, Quantity):
            new_uncertainty = self._uncertainty / np.abs(other.value)
        else:
            new_uncertainty = self._uncertainty / np.abs(other)
        
        return UncertainQuantity(result.value, result.unit, uncertainty=new_uncertainty)
    
    def __pow__(self, exponent: Union[int, float]) -> UncertainQuantity:
        """Power with uncertainty propagation."""
        result = super().__pow__(exponent)
        
        # σ_result = |n * x^(n-1) * σ_x| = |n| * |result/x| * σ_x
        rel_unc = self.relative_uncertainty
        new_rel_unc = np.abs(exponent) * rel_unc
        new_uncertainty = np.abs(result.value) * new_rel_unc
        
        return UncertainQuantity(result.value, result.unit, uncertainty=new_uncertainty)
    
    def __repr__(self) -> str:
        """String representation."""
        return f"UncertainQuantity({self.magnitude}, '{self._unit}', uncertainty={self._uncertainty})"
    
    def __str__(self) -> str:
        """Human-readable string."""
        if self._value.shape == ():
            return f"{self.magnitude:.6g} ± {self._uncertainty.item():.6g} {self._unit}"
        return f"{self.magnitude} ± {self._uncertainty} {self._unit}"
    
    def __format__(self, format_spec: str) -> str:
        """Format uncertain quantity."""
        if format_spec:
            val_str = self._value.__format__(format_spec)
            unc_str = self._uncertainty.__format__(format_spec)
            return f"{val_str} ± {unc_str} {self._unit}"
        return str(self)
