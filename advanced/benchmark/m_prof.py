"""
The memory_profiler module summarizes, in a way similar to line_profiler, the
memory usage of the process.
Terminal commands: 
$ mprof run m_prof.py
$ mprof plot
$ python -m memory_profiler m_prof.py
"""
from random import uniform
from particle import Particle, ParticleSimulator


@profile # type: ignore
def benchmark_memory():
    particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for i in range(100000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)


if __name__ == "__main__":
    benchmark_memory()


"""
$ python -m memory_profiler m_prof.py
Filename: C:\Users\lcyc2\dev\python\advanced\benchmark\particle.py

Filename: m_prof.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14   55.121 MiB   55.121 MiB           1   @profile
    15                                         def benchmark_memory():
    16   80.891 MiB   25.770 MiB      100003       particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for i in range(100000)]
    17   80.891 MiB    0.000 MiB           1       simulator = ParticleSimulator(particles)
    18   80.922 MiB    0.031 MiB           1       simulator.evolve(0.001)

- Line #: represents the line number of the code that has been profiled.
- Mem usage: the memory usage of the Python interpreter after that line has been executed.
- Increment: the difference in memory of the current line with respect to the last one.
- Line Contents: prints the code that has been profiled.
- From the Increment column, we can see that 100,000 Particle objects take 25.770 MiB of memory.


After we added __slots__ = ('x', 'y', 'ang_vel')
Filename: m_prof.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14   54.848 MiB   54.848 MiB           1   @profile
    15                                         def benchmark_memory():
    16   72.004 MiB   17.156 MiB      100003       particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for i in range(100000)]
    17   72.004 MiB    0.000 MiB           1       simulator = ParticleSimulator(particles)
    18   72.035 MiB    0.031 MiB           1       simulator.evolve(0.001)

- After we added __slots__, we saved about 10 MiB of memory.
"""
