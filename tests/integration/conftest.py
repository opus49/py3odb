"""Fixture support for integration tests."""
import pathlib
import pytest


@pytest.fixture(name="db_file")
def db_file_fixture():
    """Get the fully qualified path to the sample odb file."""
    return str(pathlib.Path(__file__).parent.parent.parent / "resources" / "sample.odb")
