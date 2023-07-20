"""
Database-style operations with Pandas
    - index operations in Pandas makes it suitable for database style manipulations
    - counting, joining, grouping and aggregations
    - Mapping:
      - pd.Series.map
      - pd.Series.apply
      - pd.Series.applymap
"""
import pandas as pd
import numpy as np
from indexing import df

# Transformation made easy on both pd.Series and pd.DataFrame
np.log(df.sys_initial)  # Logarithm of a series
df.sys_initial**2  # Square a series
np.log(df)  # Logarithm of a dataframe
df**2  # Square of a dataframe

# Matching index
a = pd.Series([1, 2, 3], index=["a", "b", "c"])
b = pd.Series([4, 5, 6], index=["a", "b", "c"])
a + b
# Result:
# a 5
# b 7
# c 9
# dtype: int64

# Mismatching index
b = pd.Series([4, 5, 6], index=["a", "b", "d"])
# Result:
# a 5.0
# b 7.0
# c NaN
# d NaN
# dtype: float64


def superstar(x):
    return "*" + str(x) + "*"


a.map(superstar)
# Result:
# a *1*
# b *2*
# c *3*
# dtype: object

apply_map = df.applymap(superstar)
print(apply_map)

# df.apply(superestar, axis=0 or 1)
# 0 corresponds to columns
# 1 corresponds to rows

axis_0 = df.apply(superstar, axis=0)
print(axis_0)

axis_1 = df.apply(superstar, axis=1)
print(axis_1)


# numexpr-style expressions
ev = df.eval("sys_final - sys_initial")
print(ev)

# assignment operation
delta = df.eval("sys_delta = sys_final - sys_initial", inplace=False)
print(delta)
