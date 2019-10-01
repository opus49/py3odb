"""Tests for odbsql module"""
import importlib
import pytest
from ..context import odbql


def test_library_failure(monkeypatch):
    """Test that missing libOdb raises an error."""
    def return_none(*args):
        """Umm..... don't return anything."""
        return None
    monkeypatch.setattr("ctypes.util.find_library", return_none)
    with pytest.raises(OSError):
        importlib.reload(odbql)
