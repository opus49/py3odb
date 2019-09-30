"""Fixture support for integration tests."""
import pathlib
import pytest


@pytest.fixture(name="sample_file")
def sample_file_fixture():
    """Get the fully qualified path to the sample odb file."""
    return str(pathlib.Path(__file__).parent.parent.parent / "resources" / "sample.odb")
