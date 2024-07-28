"""Multiple Regression

StandardScaler: Standardize features by removing the mean and scaling
to unit variance.
The standard score of a sample x is calculated as:
z = (x - u) / s
where u is the mean of the training samples or zero if with_mean=False,
and s is the standard deviation of the training samples or one if
with_std=False.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler


file_path = os.path.join(os.getcwd(), "cars.xls")

df = pd.read_excel(file_path)

df1 = df[["Mileage", "Price"]]
bins = np.arange(0, 50000, 10000)
groups = df1.groupby(pd.cut(df1["Mileage"], bins)).mean()
print(groups.head())
groups["Price"].plot.line()
plt.show()


scale = StandardScaler()

X = df[["Mileage", "Cylinder", "Doors"]]
y = df["Price"]

print("x: ", X)
print("y: ", y)
print(
    'X[["Mileage", "Cylinder", "Doors"]].values: \n',
    X[["Mileage", "Cylinder", "Doors"]].values,
)


# fit_transform(X[, y]):  Fit to data, then transform it.
# Fits transformer to X and y with optional parameters fit_params and
# returns a transformed version of X between -1 and +1 into a normal
# distribution
X[["Mileage", "Cylinder", "Doors"]] = scale.fit_transform(
    X[["Mileage", "Cylinder", "Doors"]].values
)

# Add a constant column to our model so we can have a Y-intercept
# It's just a column of 1.0 for all the rows in our data
X = sm.add_constant(X)

print("X: \n", X)

# OLS: Ordinary Least Squares
# endog: array -- A 1-d endogenous response variable. The dependent variable.
# exog: array -- A nobs x k array where nobs is the number of observations
# and k is the number of regressors.
est = sm.OLS(y, X).fit()

print("est.summary(): \n", est.summary())


# OLS Regression Results
# ==============================================================================
# Dep. Variable:                  Price   R-squared:                       0.360
# Model:                            OLS   Adj. R-squared:                  0.358
# Method:                 Least Squares   F-statistic:                     150.0
# Date:                Sat, 19 Aug 2023   Prob (F-statistic):           3.95e-77
# Time:                        22:51:41   Log-Likelihood:                -8356.7
# No. Observations:                 804   AIC:                         1.672e+04
# Df Residuals:                     800   BIC:                         1.674e+04
# Df Model:                           3
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const       2.134e+04    279.405     76.388      0.000    2.08e+04    2.19e+04
# Mileage    -1272.3412    279.567     -4.551      0.000   -1821.112    -723.571
# Cylinder    5587.4472    279.527     19.989      0.000    5038.754    6136.140
# Doors      -1404.5513    279.446     -5.026      0.000   -1953.085    -856.018
# ==============================================================================
# Omnibus:                      157.913   Durbin-Watson:                   0.069
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              257.529
# Skew:                           1.278   Prob(JB):                     1.20e-56
# Kurtosis:                       4.074   Cond. No.                         1.03
# ==============================================================================


# How would you use this to make an actual prediction? Start by scaling your
# multiple feature variables into the same scale used to train the model, then
# just call est.predict() on the scaled features
mean_price_by_doors = y.groupby(df.Doors).mean()
print("mean_price_by_doors: ", mean_price_by_doors)
# mean_price_by_doors:  Doors
# 2    23807.135520
# 4    20580.670749


# Use the following fake data predict the price
fake_mileage = 45000
fake_cylinder = 8
fake_doors = 4
scaled = scale.transform([[fake_mileage, fake_cylinder, fake_doors]])
scaled = np.insert(scaled[0], 0, 1)  # Need to add that constant column in.
print("scaled: \n", scaled)

# Return linear predicted values from a design matrix.
predicted = est.predict(scaled)
print("predicted: \n", predicted)
