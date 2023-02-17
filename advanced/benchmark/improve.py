"""
Particle Application to be used for Benchmarking and Profiling
"""
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Particle:
    """
    A particle will follow a circular tragectory
    x: value of the particle in the x-axis
    y: value of the particle in the y-axis
    ang_vel: angular velocity of the particle
    """

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

    @profile
    def evolve_fast(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        # Loop order is changed
        for p in self.particles:
            t_x_ang = timestep * p.ang_vel
            for i in range(nsteps):
                sum = p.x**2 + p.y**2
                p.x = p.x - t_x_ang * p.y / np.sqrt(sum)
                p.y = p.y + t_x_ang * p.x / np.sqrt(sum)


def visualize(simulator):
    """
    It takes a particle ParticleSimulator instance as an argument and
    displays the tragectory in an animated plot.
    1. Set up the axes and use the plot function to display the particles.
    2. The initialization function updates the x and y coordinates
    3. Create a FuncAnimation instance
    4. Run the animation with plt.show()
    """
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    (line,) = ax.plot(X, Y, "ro")
    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        line.set_data([], [])
        return (line,)  # The comma is important!

    def animate(i):
        # We let the particle evolve for 0.01 time units
        simulator.evolve_fast(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return (line,)

    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10)

    plt.show()


def test_visualize():
    """
    Animates a system of three particles rotating in different directions.
    """
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3),
    ]

    simulator = ParticleSimulator(particles)
    visualize(simulator)


if __name__ == "__main__":
    test_visualize()
