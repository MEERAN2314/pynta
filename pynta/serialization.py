"""Serialization support for Pynta quantities."""

import json
import pickle
from typing import Any, Dict
import numpy as np
from pynta.quantity import Quantity
from pynta.unit import Unit


def quantity_to_dict(quantity: Quantity) -> Dict[str, Any]:
    """
    Convert a Quantity to a dictionary.
    
    Args:
        quantity: Quantity to serialize
        
    Returns:
        Dictionary representation
        
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> d = quantity_to_dict(q)
        >>> print(d)
        {'value': 100, 'unit': 'meter', 'type': 'Quantity'}
    """
    value = quantity.magnitude
    if isinstance(value, np.ndarray):
        value = value.tolist()
    
    return {
        'value': value,
        'unit': str(quantity.unit),
        'type': 'Quantity',
        'version': '1.0'
    }


def dict_to_quantity(data: Dict[str, Any]) -> Quantity:
    """
    Convert a dictionary to a Quantity.
    
    Args:
        data: Dictionary representation
        
    Returns:
        Quantity object
        
    Examples:
        >>> d = {'value': 100, 'unit': 'meter', 'type': 'Quantity'}
        >>> q = dict_to_quantity(d)
    """
    if data.get('type') != 'Quantity':
        raise ValueError("Dictionary does not represent a Quantity")
    
    value = data['value']
    if isinstance(value, list):
        value = np.array(value)
    
    return Quantity(value, data['unit'])


def quantity_to_json(quantity: Quantity, **kwargs) -> str:
    """
    Convert a Quantity to JSON string.
    
    Args:
        quantity: Quantity to serialize
        **kwargs: Additional arguments for json.dumps
        
    Returns:
        JSON string
        
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> json_str = quantity_to_json(q)
    """
    data = quantity_to_dict(quantity)
    return json.dumps(data, **kwargs)


def json_to_quantity(json_str: str) -> Quantity:
    """
    Convert a JSON string to a Quantity.
    
    Args:
        json_str: JSON string
        
    Returns:
        Quantity object
        
    Examples:
        >>> json_str = '{"value": 100, "unit": "meter", "type": "Quantity"}'
        >>> q = json_to_quantity(json_str)
    """
    data = json.loads(json_str)
    return dict_to_quantity(data)


def save_quantity(quantity: Quantity, filename: str, format: str = 'json') -> None:
    """
    Save a Quantity to a file.
    
    Args:
        quantity: Quantity to save
        filename: Output filename
        format: Format ('json' or 'pickle')
        
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> save_quantity(q, 'distance.json')
    """
    if format == 'json':
        with open(filename, 'w') as f:
            json.dump(quantity_to_dict(quantity), f, indent=2)
    elif format == 'pickle':
        with open(filename, 'wb') as f:
            pickle.dump(quantity, f)
    else:
        raise ValueError(f"Unknown format: {format}")


def load_quantity(filename: str, format: str = 'json') -> Quantity:
    """
    Load a Quantity from a file.
    
    Args:
        filename: Input filename
        format: Format ('json' or 'pickle')
        
    Returns:
        Quantity object
        
    Examples:
        >>> q = load_quantity('distance.json')
    """
    if format == 'json':
        with open(filename, 'r') as f:
            data = json.load(f)
        return dict_to_quantity(data)
    elif format == 'pickle':
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError(f"Unknown format: {format}")


class QuantityEncoder(json.JSONEncoder):
    """
    JSON encoder for Quantity objects.
    
    Examples:
        >>> q = Quantity(100, 'meter')
        >>> json.dumps({'distance': q}, cls=QuantityEncoder)
    """
    
    def default(self, obj):
        """Encode Quantity objects."""
        if isinstance(obj, Quantity):
            return quantity_to_dict(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        return super().default(obj)


def quantity_decoder(dct: Dict[str, Any]) -> Any:
    """
    JSON decoder for Quantity objects.
    
    Args:
        dct: Dictionary from JSON
        
    Returns:
        Quantity if dict represents one, otherwise the dict itself
        
    Examples:
        >>> json.loads(json_str, object_hook=quantity_decoder)
    """
    if dct.get('type') == 'Quantity':
        return dict_to_quantity(dct)
    return dct
