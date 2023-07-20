"""
We need to optimize function evolve in particle.py, we can use the line_profiler module that provides 
information on how time is spent in a line-by-line fashion.

We added @profile decorator to the evolve function.
Terminal command: kernprof -l -v particle.py

###############################################################################################################

Wrote profile results to particle.py.lprof
Timer unit: 1e-06 s

Total time: 0.835068 s
File: particle.py
Function: evolve at line 32

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    32                                               @profile  # NOQA
    33                                               def evolve(self, dt):
    34       158        159.5      1.0      0.0          timestep = 0.00001
    35       158        231.5      1.5      0.0          nsteps = int(dt / timestep)
    36    157842      25347.4      0.2      3.0          for i in range(nsteps):
    37    473526      72140.2      0.2      8.6              for p in self.particles:
    38                                                           # 1. calculate the direction
    39    473526     183186.7      0.4     21.9                  norm = (p.x**2 + p.y**2) ** 0.5
    40    473526      95166.5      0.2     11.4                  v_x = -p.y / norm
    41    473526      81352.4      0.2      9.7                  v_y = p.x / norm
    42
    43                                                           # 2. calculate the displacement
    44    473526      95147.9      0.2     11.4                  d_x = timestep * p.ang_vel * v_x
    45    473526      92986.5      0.2     11.1                  d_y = timestep * p.ang_vel * v_y
    46
    47    473526      96137.5      0.2     11.5                  p.x += d_x
    48    473526      93211.6      0.2     11.2                  p.y += d_y
    49                                                           # 3. repeat for all time steps

###############################################################################################################

Interpretation

- Line #: The number of the line that was run
- Hits: The number of times that line was run
- Time: The execution time of the line in microseconds (Time)
- Per Hit: Time/hits
- % Time: Fraction of the total time spent executing that line
- Line Contents: The content of the line
- Total time: 99.8

###############################################################################################################

Improve the algorithm and use evolve_fast function
Terminal command: kernprof -l -v improve.py

Wrote profile results to improve.py.lprof
Timer unit: 1e-06 s

Total time: 1.06035 s
File: improve.py
Function: evolve_fast at line 33

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    33                                               @profile
    34                                               def evolve_fast(self, dt):
    35       181        331.8      1.8      0.0          timestep = 0.00001
    36       181        270.8      1.5      0.0          nsteps = int(dt / timestep)
    37                                                   # Loop order is changed
    38       543        232.3      0.4      0.0          for p in self.particles:
    39       543        282.4      0.5      0.0              t_x_ang = timestep * p.ang_vel
    40    542457      87952.4      0.2      8.3              for i in range(nsteps):
    41    542457     177133.4      0.3     16.7                  sum = p.x**2 + p.y**2
    42    542457     399597.6      0.7     37.7                  p.x = p.x - t_x_ang * p.y / np.sqrt(sum)
    43    542457     394549.7      0.7     37.2                  p.y = p.y + t_x_ang * p.x / np.sqrt(sum)

- It isn't improved very much as more time is spent on the the last two lines
- Total time: 99.9
"""
