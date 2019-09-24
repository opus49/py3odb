"""Integration test for INSERT and SELECT."""
import pathlib
from ..context import py3odb


def test_read_sample():
    """Read a sample database."""
    db_file = pathlib.Path(__file__).parent.parent.parent / "resources" / "sample.odb"
    print(f"Opening {db_file} for reading.")
    conn = py3odb.connect(f"{db_file}")
    cur = conn.cursor()
    print("Executing SELECT")
    cur.execute(f"SELECT * FROM '{db_file}'")
    print("Fetching a row")
    data = cur.fetchone()
    print(f"{data}")
    conn.close()
