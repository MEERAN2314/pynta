"""Batch operations for multiple quantities."""

from typing import List, Union, Dict
from unifyt.quantity import Quantity
from unifyt.unit import Unit
import numpy as np


class BatchConverter:
    """
    Batch converter for multiple quantities.
    
    Examples:
        >>> converter = BatchConverter()
        >>> quantities = [Quantity(100, 'meter'), Quantity(50, 'foot')]
        >>> results = converter.convert_all(quantities, 'kilometer')
    """
    
    def __init__(self):
        """Initialize batch converter."""
        pass
    
    def convert_all(
        self,
        quantities: List[Quantity],
        target_unit: Union[str, Unit]
    ) -> List[Quantity]:
        """
        Convert multiple quantities to the same target unit.
        
        Args:
            quantities: List of quantities to convert
            target_unit: Target unit for all conversions
        
        Returns:
            List of converted quantities
        
        Examples:
            >>> converter = BatchConverter()
            >>> quantities = [Quantity(100, 'meter'), Quantity(1, 'kilometer')]
            >>> results = converter.convert_all(quantities, 'meter')
            >>> print(results)  # [100 meter, 1000 meter]
        """
        return [q.to(target_unit) for q in quantities]
    
    def convert_dict(
        self,
        quantity_dict: Dict[str, Quantity],
        target_unit: Union[str, Unit]
    ) -> Dict[str, Quantity]:
        """
        Convert a dictionary of quantities to the same target unit.
        
        Args:
            quantity_dict: Dictionary of {name: quantity}
            target_unit: Target unit for all conversions
        
        Returns:
            Dictionary with converted quantities
        
        Examples:
            >>> converter = BatchConverter()
            >>> quantities = {'a': Quantity(100, 'meter'), 'b': Quantity(1, 'km')}
            >>> results = converter.convert_dict(quantities, 'meter')
        """
        return {name: q.to(target_unit) for name, q in quantity_dict.items()}
    
    def sum_quantities(
        self,
        quantities: List[Quantity],
        target_unit: Union[str, Unit] = None
    ) -> Quantity:
        """
        Sum multiple quantities (must have compatible units).
        
        Args:
            quantities: List of quantities to sum
            target_unit: Optional target unit for result
        
        Returns:
            Sum of all quantities
        
        Examples:
            >>> converter = BatchConverter()
            >>> quantities = [Quantity(100, 'meter'), Quantity(50, 'meter')]
            >>> total = converter.sum_quantities(quantities)
            >>> print(total)  # 150 meter
        """
        if not quantities:
            raise ValueError("Cannot sum empty list of quantities")
        
        # Use first quantity's unit as reference
        reference_unit = quantities[0].unit
        
        # Convert all to reference unit and sum
        total_value = sum(q.to(reference_unit).value for q in quantities)
        result = Quantity(total_value, reference_unit)
        
        # Convert to target unit if specified
        if target_unit is not None:
            result = result.to(target_unit)
        
        return result
    
    def mean_quantities(
        self,
        quantities: List[Quantity],
        target_unit: Union[str, Unit] = None
    ) -> Quantity:
        """
        Calculate mean of multiple quantities.
        
        Args:
            quantities: List of quantities
            target_unit: Optional target unit for result
        
        Returns:
            Mean of all quantities
        
        Examples:
            >>> converter = BatchConverter()
            >>> quantities = [Quantity(100, 'meter'), Quantity(200, 'meter')]
            >>> mean = converter.mean_quantities(quantities)
            >>> print(mean)  # 150 meter
        """
        if not quantities:
            raise ValueError("Cannot calculate mean of empty list")
        
        total = self.sum_quantities(quantities)
        result = total / len(quantities)
        
        if target_unit is not None:
            result = result.to(target_unit)
        
        return result
    
    def min_quantity(
        self,
        quantities: List[Quantity],
        target_unit: Union[str, Unit] = None
    ) -> Quantity:
        """
        Find minimum quantity.
        
        Args:
            quantities: List of quantities
            target_unit: Optional target unit for result
        
        Returns:
            Minimum quantity
        """
        if not quantities:
            raise ValueError("Cannot find min of empty list")
        
        reference_unit = quantities[0].unit
        values = [q.to(reference_unit).value for q in quantities]
        min_idx = np.argmin(values)
        result = quantities[min_idx]
        
        if target_unit is not None:
            result = result.to(target_unit)
        
        return result
    
    def max_quantity(
        self,
        quantities: List[Quantity],
        target_unit: Union[str, Unit] = None
    ) -> Quantity:
        """
        Find maximum quantity.
        
        Args:
            quantities: List of quantities
            target_unit: Optional target unit for result
        
        Returns:
            Maximum quantity
        """
        if not quantities:
            raise ValueError("Cannot find max of empty list")
        
        reference_unit = quantities[0].unit
        values = [q.to(reference_unit).value for q in quantities]
        max_idx = np.argmax(values)
        result = quantities[max_idx]
        
        if target_unit is not None:
            result = result.to(target_unit)
        
        return result
    
    def normalize_units(
        self,
        quantities: List[Quantity],
        target_unit: Union[str, Unit] = None
    ) -> List[Quantity]:
        """
        Normalize all quantities to the same unit.
        
        Args:
            quantities: List of quantities with potentially different units
            target_unit: Target unit (default: first quantity's unit)
        
        Returns:
            List of quantities all in the same unit
        
        Examples:
            >>> converter = BatchConverter()
            >>> quantities = [
            ...     Quantity(100, 'meter'),
            ...     Quantity(1, 'kilometer'),
            ...     Quantity(50, 'foot')
            ... ]
            >>> normalized = converter.normalize_units(quantities, 'meter')
        """
        if not quantities:
            return []
        
        if target_unit is None:
            target_unit = quantities[0].unit
        
        return self.convert_all(quantities, target_unit)


def convert_batch(
    quantities: List[Quantity],
    target_unit: Union[str, Unit]
) -> List[Quantity]:
    """
    Quick batch conversion function.
    
    Args:
        quantities: List of quantities to convert
        target_unit: Target unit
    
    Returns:
        List of converted quantities
    
    Examples:
        >>> quantities = [Quantity(100, 'meter'), Quantity(1, 'kilometer')]
        >>> results = convert_batch(quantities, 'meter')
    """
    converter = BatchConverter()
    return converter.convert_all(quantities, target_unit)


def sum_batch(quantities: List[Quantity]) -> Quantity:
    """
    Quick batch sum function.
    
    Args:
        quantities: List of quantities to sum
    
    Returns:
        Sum of all quantities
    
    Examples:
        >>> quantities = [Quantity(100, 'meter'), Quantity(50, 'meter')]
        >>> total = sum_batch(quantities)
    """
    converter = BatchConverter()
    return converter.sum_quantities(quantities)
