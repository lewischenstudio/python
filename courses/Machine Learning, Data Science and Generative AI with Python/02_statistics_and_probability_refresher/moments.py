"""Moments: Mean, Variance, Skew, Kurtosis"""

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

print(np.mean(vals))

print(np.var(vals))

# The third moment is skew - since our data is nicely centered around 0,
# it should be almost 0:
print(sp.skew(vals))
# -0.039210719172605074

# The fourth moment is "kurtosis", which describes the shape of the tail.
# For a normal distribution, this is 0
print(sp.kurtosis(vals))
# -0.004505084880528365


vals = np.append(vals, [10000])
vals = np.append(vals, [10000])
vals = np.append(vals, [10000])
vals = np.append(vals, [10000])
vals = np.append(vals, [10000])
vals = np.append(vals, [10000])

print(sp.skew(vals))
# 40.800078597491634

print(sp.kurtosis(vals))
# 1662.6533729320074
