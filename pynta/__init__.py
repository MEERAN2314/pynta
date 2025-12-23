"""
Pynta - A powerful library for unit conversion and calculations.

Combines the best features of Pint and Unyt for intuitive and high-performance
unit handling in Python.
"""

from pynta.quantity import Quantity
from pynta.unit import Unit
from pynta.unit_registry import UnitRegistry
from pynta.dimensions import Dimension
from pynta.context import UnitContext
from pynta import constants
from pynta import utils
from pynta.serialization import (
    quantity_to_dict,
    dict_to_quantity,
    quantity_to_json,
    json_to_quantity,
    save_quantity,
    load_quantity,
    QuantityEncoder,
    quantity_decoder,
)

__version__ = "0.1.0"
__all__ = [
    "Quantity",
    "Unit",
    "UnitRegistry",
    "Dimension",
    "UnitContext",
    "constants",
    "utils",
    "quantity_to_dict",
    "dict_to_quantity",
    "quantity_to_json",
    "json_to_quantity",
    "save_quantity",
    "load_quantity",
    "QuantityEncoder",
    "quantity_decoder",
]

# Create default unit registry
default_registry = UnitRegistry()
