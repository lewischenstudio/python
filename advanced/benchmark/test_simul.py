"""
Pytest is a testing framework is a set of tools that simplifies writing, executing, and debugging tests and provides 
rich reports and summaries of the test results.
"""
from particle import Particle, ParticleSimulator


def test_evolve(benchmark):
    """
    Command: pytest path/to/module.py::function_name
    Execute your test as a benchmark using the pytest-benchmark plugin with bencharmark fixuture
    Remember to do pip install pytest-benchmark
    """
    particles = [Particle(0.3, 0.5, +1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, +3)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a - b) < eps

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)

    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)

    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)

    benchmark(simulator.evolve, 0.1)


"""
---------------------------------------------- benchmark: 1 tests ---------------------------------------------
Name (time in ms)         Min      Max     Mean  StdDev   Median     IQR  Outliers      OPS  Rounds  Iterations
---------------------------------------------------------------------------------------------------------------
test_evolve           10.2526  13.4765  11.1543  0.5256  11.0365  0.4054      14;9  89.6515      87           1
---------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean


###############################################################################################################

Interpretation
- the benchmark was run 87 times (column Rounds)
- its timings ranged between 10 and 13 ms (Min and Max)
- the Average and Median times  were about 30 ms (Mean)
- pytest-benchmark: http:// pytest- benchmark. readthedocs. io/ en/ stable/ usage. html.
"""
