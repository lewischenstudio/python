"""
Caching and memoization
    - Caching is to store expensive results in a temporary location called cache
    - Web applications use caching a lot
    - A type of caching is memoization, referring to storing and reusing the results of the previous function
      calls in an application.
    - Dynamic programming is a technique where other algorithms can take advantage of memoization to gain impressive
      performance improvements.
    - functools.iru_cache
      - args: maxsize
      - methods: cache_info
"""

from functools import lru_cache
import timeit

# To restrict the size of the cache, one can set the number of elements that we intend to maintain through the max_size
# argument.


@lru_cache(maxsize=16)
def sum2(a, b):
    print("Calculating {} + {}".format(a, b))
    return a + b


print(sum2(1, 2))

print(sum2(1, 2))

print(sum2.cache_info())


setup_code = """
from functools import lru_cache
def fibonacci(n):
    if n < 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci_memoized = lru_cache(maxsize=None)(fibonacci)
"""

results = timeit.repeat("fibonacci_memoized(20)", setup=setup_code, repeat=1000, number=1)
print("Fibonacci took {:.2f} us".format(min(results)))
