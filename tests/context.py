"""Import to add py3odb to PYTHONPATH"""
import pathlib
import sys


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
