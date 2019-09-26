"""Import to add project directory to PYTHONPATH"""
import pathlib
import sys


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import py3odb # noqa: 401,402 # pylint: disable=wrong-import-position,unused-import
import py3odb.odbql as odbql # noqa: 401,402 # pylint: disable=wrong-import-position,unused-import
