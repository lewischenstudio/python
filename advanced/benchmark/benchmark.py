"""
Benchmarks are very useful to keep score of how fast our program is with each new 
version that we implement.
"""
from particle import Particle, ParticleSimulator
from random import uniform


def benchmark():
    particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for i in range(1000)]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


if __name__ == "__main__":
    benchmark()
