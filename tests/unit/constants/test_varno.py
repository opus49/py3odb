"""Tests for varno module."""
from ...context import py3odb


def test_get_name():
    """Test the get code method."""
    assert py3odb.constants.Varno.get_name(215) == "1dvar"
    assert py3odb.constants.Varno.get_name(108) == "pmsl"
    assert py3odb.constants.Varno.get_name(61) == "ww"
    assert py3odb.constants.Varno.get_name(-1) == "unknown"


def test_get_code():
    """Test the get_code method."""
    assert py3odb.constants.Varno.get_code("aerod") == 174
    assert py3odb.constants.Varno.get_code("rh") == 29
    assert py3odb.constants.Varno.get_code("soilm") == 180
    assert py3odb.constants.Varno.get_code("foo") == "unknown"


def test_get_desc():
    """Test the get_desc method."""
    assert py3odb.constants.Varno.get_desc("airframe_icing") == "airframe icing"
    assert py3odb.constants.Varno.get_desc("od") == "optical depth"
    assert py3odb.constants.Varno.get_desc("spsp1") == "special phenomena (spsp)#1"
    assert py3odb.constants.Varno.get_desc("foo") == "unknown"
