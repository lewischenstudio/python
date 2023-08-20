"""Linear Regression"""

import matplotlib.pyplot as plt
import numpy as np
from pylab import scatter
from scipy import stats

mean = 3.0
std = 1.0
pageSpeeds = np.random.normal(mean, std, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

scatter(pageSpeeds, purchaseAmount)
plt.show()


slope, intercept, r_value, p_value, std_err = stats.linregress(
    pageSpeeds, purchaseAmount
)

# R-squared value shows a really good fit
r_squared = r_value**2
print("r_squared: ", r_squared)

# slope
print("slope: ", slope)

# intercept
print("intercept: ", intercept)

# p_value
print("p_value: ", p_value)

# std_err
print("std_err: ", std_err)


# plot predicted values vs. observed
def predict(x):
    return slope * x + intercept


fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c="r")
plt.show()


# Activity
# Try increasing the random variation in the test data, and see what effect it
# has on the r-squared error value.

mean = 3.0
std = 10.0
pageSpeeds = np.random.normal(mean, std, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

slope, intercept, r_value, p_value, std_err = stats.linregress(
    pageSpeeds, purchaseAmount
)

print("std_err: ", std_err)

# std_err:  0.009525908697963818
# std_err:  0.0009265786466186493
# By increasing the standard deviation in page speed, the std_err is decreased
# by 10 fold.
