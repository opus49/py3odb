"""Tests for varno module."""
from ...context import py3odb


def test_get_code():
    """Test the get code method."""
    assert py3odb.constants.Varno.get_code(215) == "1dvar"
    assert py3odb.constants.Varno.get_code(108) == "pmsl"
    assert py3odb.constants.Varno.get_code(61) == "ww"
    assert py3odb.constants.Varno.get_code(-1) == "unknown"


def test_get_varno():
    """Test the get_varno method."""
    assert py3odb.constants.Varno.get_varno("aerod") == 174
    assert py3odb.constants.Varno.get_varno("rh") == 29
    assert py3odb.constants.Varno.get_varno("soilm") == 180
    assert py3odb.constants.Varno.get_varno("foo") == "unknown"


def test_get_desc():
    """Test the get_desc method."""
    assert py3odb.constants.Varno.get_desc("airframe_icing") == "airframe icing"
    assert py3odb.constants.Varno.get_desc("od") == "optical depth"
    assert py3odb.constants.Varno.get_desc("spsp1") == "special phenomena (spsp)#1"
    assert py3odb.constants.Varno.get_desc("foo") == "unknown"
