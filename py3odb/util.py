"""Utility modules for py3odb."""
from contextlib import contextmanager
import os
import sys


@contextmanager
def suppress_stdout():
    """
    Suppresses all standard output.  Useful for blocking output from ctypes.
    See https://stackoverflow.com/a/4178672 for more details.
    """
    sys.stdout.flush()
    with open(os.devnull, "w") as devnull:
        old_stdout_fileno = os.dup(sys.stdout.fileno())
        os.dup2(devnull.fileno(), 1)
        try:
            yield
        finally:
            os.dup2(old_stdout_fileno, 1)
            os.close(old_stdout_fileno)
