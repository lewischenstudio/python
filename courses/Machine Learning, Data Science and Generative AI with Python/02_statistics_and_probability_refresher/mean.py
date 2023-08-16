"""Mean, Median, Mode, and introducing NumPy"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Mean vs Median

incomes = np.random.normal(27000, 15000, 10000)
print(np.mean(incomes))

# %matplotlib inline (for ipython)
plt.hist(incomes, 50)
plt.show()

np.median(incomes)

incomes = np.append(incomes, [100000000])

print(np.median(incomes))

print(np.mean(incomes))


# Mode
ages = np.random.randint(18, high=90, size=500)
# print(ages)

print(stats.mode(ages))


# Exercise

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)
plt.show()

print(np.mean(incomes))

print(np.median(incomes))

incomes = np.append(incomes, [100000000])

print(np.mean(incomes))

print(np.median(incomes))
