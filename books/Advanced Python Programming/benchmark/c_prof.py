"""
Profiling is the technique that allows us to pinpoint the most resource-intensive spots in an  application.
It allows to identify the parts of the code that need to be tuned for performance. There are two modules:
profile and cProfile.
"""

from benchmark import benchmark
import cProfile


def profiling_simulation():
    pr = cProfile.Profile()
    pr.enable()
    benchmark()
    pr.disable()
    pr.print_stats()


if __name__ == "__main__":
    profiling_simulation()

"""
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 benchmark.py:10(<listcomp>)
        1    0.000    0.000    3.411    3.411 benchmark.py:9(benchmark)
     1000    0.000    0.000    0.000    0.000 particle.py:16(__init__)
        1    0.000    0.000    0.000    0.000 particle.py:29(__init__)
        1    3.410    3.410    3.410    3.410 particle.py:32(evolve)
     3000    0.001    0.000    0.001    0.000 random.py:511(uniform)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     3000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

###############################################################################################################

Interpretation
- ncalls: The number of times the function was called.
- tottime: The total time spent in the function without taking into account the calls to other functions.
- cumtime: The time in the function including other function calls.
- percall: The time spent for a single call of the function--it can be obtained by dividing the total or
           cumulative time by the number of calls.
- filename:lineno: The filename and corresponding line numbers. This information is not available when
                   calling C extensions modules.
- particle.py:32(evolve) means that it is the evolve function in particle.py that needs tunning
"""
