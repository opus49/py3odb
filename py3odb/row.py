"""Module for Row class."""

from collections import OrderedDict
from collections.abc import Mapping


class Row(Mapping):
    """An immutable sequence object representing an SQL result row."""
    def __init__(self, *args, **kwargs):
        # As of Python 3.6, for CPython at least, dictionaries are ordered.
        # However, this is an implementation detail, not a feature.  Default
        # insert ordering of dict did not become a feature until Python 3.7.
        # To ensure correct functionality across Python 3.6 implementations,
        # the underlying __dict__ needs to be an OrderedDict.
        self.__dict__ = OrderedDict()
        self.__dict__.update(*args, **kwargs)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.__dict__[self.keys()[index]]
        return self.__dict__[index]

    def __iter__(self):
        return iter(self.__dict__.values())

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return f"Row({repr(dict(self.__dict__))})"

    def __str__(self):
        return str(tuple(self.__dict__.values()))

    def keys(self):
        """Returns the list of column names."""
        return list(self.__dict__.keys())
