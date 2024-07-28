"""Polynomial Regression"""

import matplotlib.pyplot as plt
import numpy as np
from pylab import scatter
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

# Numpy has a handy polyfit function we can use, to let us construct an
# nth-degree polynomial model of our data that minimizes squared error.
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))


# Plot the fit
xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c="r")
plt.show()


# Measure the r-squared error
r2 = r2_score(y, p4(x))
print(r2)


# Activity
# Try different polynomial orders. Can you get a better fit with higher orders?
# y = 4x^2 + 3x + 100 2nd order polynomial, expect r-squared to be 1.0
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 4 * pageSpeeds**2 + 3 * pageSpeeds + 100

scatter(pageSpeeds, purchaseAmount)
plt.show()

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p2 = np.poly1d(np.polyfit(x, y, 2))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p2(xp), c="r")
plt.show()

# Measure the r-squared error
r2 = r2_score(y, p2(x))
print(r2)
# 1.0
