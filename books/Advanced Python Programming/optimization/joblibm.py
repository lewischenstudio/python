"""
Joblib provides a simple on-disk cache
    - pip install joblib
    - provides efficient memoization of functions that operate on numpy arrays
    - particularly useful in scientific and engineering applications.
"""

# import os
from joblib import Memory

memory = Memory("./cachedir")


@memory.cache
def sum2(a, b):
    return a + b
