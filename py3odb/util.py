"""Utility modules for py3odb."""
from contextlib import contextmanager
import os
import sys


@contextmanager
def suppress_stdout():
    """Suppress STDOUT.  Useful for suppressing output from ctypes."""
    sys.stdout.flush()
    with open(os.devnull, "w") as devnull:
        old_stdout_fileno = os.dup(sys.stdout.fileno())
        os.dup2(devnull.fileno(), 1)
        try:
            yield
        finally:
            os.dup2(old_stdout_fileno, 1)
