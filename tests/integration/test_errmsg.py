"""Test the integration between Cursor and odbql's errmsg."""
import pytest
from ..context import py3odb


def test_errmsg():
    """Create a database and then feed it junk."""
    conn = py3odb.connect("")
    cur = conn.cursor()
    with pytest.raises(py3odb.ProgrammingError) as err:
        cur.execute("i have no idea what i am doing")
    assert "syntax error" in str(err.value)
