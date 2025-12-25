"""
Unifyt - A powerful library for unit conversion and calculations.

Combines the best features of Pint and Unyt for intuitive and high-performance
unit handling in Python.
"""

from unifyt.quantity import Quantity
from unifyt.unit import Unit
from unifyt.unit_registry import UnitRegistry
from unifyt.dimensions import Dimension
from unifyt.context import UnitContext
from unifyt import constants
from unifyt import utils
from unifyt.serialization import (
    quantity_to_dict,
    dict_to_quantity,
    quantity_to_json,
    json_to_quantity,
    save_quantity,
    load_quantity,
    QuantityEncoder,
    quantity_decoder,
)

__version__ = "0.2.0"
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
