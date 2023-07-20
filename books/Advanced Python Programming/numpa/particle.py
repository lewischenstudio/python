"""
Rewriting the particle simulator in Numpy
"""

import time
import numpy as np
from random import uniform


class Particle:
    """
    A particle will follow a circular tragectory
    x: value of the particle in the x-axis
    y: value of the particle in the y-axis
    ang_vel: angular velocity of the particle
    """

    # add __slots__ to improve memory
    __slots__ = ("x", "y", "ang_vel")

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    """
    1. Calculate the direction of motion (v_x, v_y).
    2. Calculate the displacement (d_x, d_y)
    3. Repeat sptes 1 and 2 for enough times
    """

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        for i in range(nsteps):
            for p in self.particles:
                norm = (p.x**2 + p.y**2) ** 0.5
                v_x = -p.y / norm
                v_y = p.x / norm

                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y

    def evolve_numpy(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_vel_i = np.array([p.ang_vel for p in self.particles])

        for i in range(nsteps):
            norm_i = np.sqrt((r_i**2).sum(axis=1))
            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1
            v_i /= norm_i[:, np.newaxis]
            d_i = timestep * ang_vel_i[:, np.newaxis] * v_i
            r_i += d_i

            for i, p in enumerate(self.particles):
                p.x, p.y = r_i[i]


def benchmark(npart=100, method="python"):
    particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for i in range(npart)]

    simulator = ParticleSimulator(particles)

    if method == "python":
        simulator.evolve(0.1)
    elif method == "numpy":
        simulator.evolve_numpy(0.1)


t0 = time.time()
benchmark(1000, "python")
t1 = time.time()
print("total time: ", t1 - t0)

t0 = time.time()
benchmark(1000, "numpy")
t1 = time.time()
print("total time: ", t1 - t0)
