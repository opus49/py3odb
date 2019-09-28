"""Module for storing constant variables and static classes."""

from enum import Enum
from .varno import Varno

__all__ = [
    "Varno",
    "ColumnType"
]


class ColumnType(Enum):
    """Constant values for the various column types."""
    INTEGER = 1
    FLOAT = 2
    TEXT = 3
    BLOB = 4
    NULL = 5
    BITFIELD = 6
