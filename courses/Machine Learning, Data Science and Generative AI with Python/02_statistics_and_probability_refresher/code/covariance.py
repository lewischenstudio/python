"""Covariance and Correlation

let's say we work for an e-commerce company, and they are interested in
finding a correlation between page speed (how fast each web page renders
for a customer) and how much a customer spends.
"""

import matplotlib.pyplot as plt
import numpy as np
from pylab import mean, dot, scatter


def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

scatter(pageSpeeds, purchaseAmount)

covariance(pageSpeeds, purchaseAmount)
plt.show()


purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

covariance(pageSpeeds, purchaseAmount)
plt.show()
# Covariance is sensitive to the units used in the variables, which makes it
# difficult to interpret. Correlation normalizes everything by their standard
# deviations, giving you an easier to understand value that ranges from -1
# (for a perfect inverse correlation) to 1 (for a perfect positive correlation)


def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return (
        covariance(x, y) / stddevx / stddevy
    )  # In real life you'd check for divide by zero here


correlation(pageSpeeds, purchaseAmount)


# numpy can do all this for you with numpy.corrcoef. It returns a matrix of
# the correlation coefficients between every combination of the arrays pass in
np.corrcoef(pageSpeeds, purchaseAmount)


# We can force a perfect correlation by fabricating a totally linear
# relationship
purchaseAmount = 100 - pageSpeeds * 3

scatter(pageSpeeds, purchaseAmount)

correlation(pageSpeeds, purchaseAmount)

plt.show()
# Remember, correlation does not imply causality!
