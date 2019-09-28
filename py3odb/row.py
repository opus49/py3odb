"""Module for Row class."""

from collections.abc import Mapping


class Row(Mapping):
    """An immutable sequence object representing an SQL row."""
    def __init__(self, *args, **kwargs):
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
        return str(tuple(self.__dict__.values()))

    def keys(self):
        """Returns the list of column names."""
        return list(self.__dict__.keys())
