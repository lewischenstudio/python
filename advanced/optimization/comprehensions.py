"""
Comprehensions and generators
    - Comprehension and generator expressions are fairly optimized operations and should be preferred in place of
      explicit for-loops.
    - Comprehension and generator syntax is more compact and (most of the times) more intuitive even if the speedup
      over a standard loop is modest.
"""


# comprehension is the fastest, generator is the second, and loop is the slowest
def loop():
    res = []
    for i in range(100000):
        res.append(i * i)
    return sum(res)


def comprehension():
    return sum([i * i for i in range(100000)])


def generator():
    return sum(i * i for i in range(100000))


##############


def loop_():
    res = {}
    for i in range(100000):
        res[i] = i
    return res


def comprehension_():
    return {i: i for i in range(100000)}


################


def map_comprehension(numbers):
    a = [n * 2 for n in numbers]
    b = [n**2 for n in a]
    c = [n**0.33 for n in b]
    return max(c)


# The map function:
# 1. takes two arguments--a function and an iteratorand
# 2. returns a generator that applies the function to every element of the collection.


def map_normal(numbers):
    a = map(lambda n: n * 2, numbers)
    b = map(lambda n: n**2, a)
    c = map(lambda n: n**0.33, b)
    return max(c)


# %load_ext memory_profiler
# numbers = range(1000000)
# %memit map_comprehension(numbers)
# peak memory: 166.33 MiB, increment: 102.54 MiB
# %memit map_normal(numbers)
# peak memory: 71.04 MiB, increment: 0.00 MiB
