"""
Pandas
    - Pandas is a library to analyze datasets in a seamless performant way.
    - pandas.Series
    - pandas.DataFrame
"""

import pandas as pd

# Series
patients = [0, 1, 2, 3]
effective = [True, True, False, False]
effective_series = pd.Series(effective, index=patients)


# DateFrame
patients = ["a", "b", "c", "d"]
effective = [True, True, False, False]
effective_series = pd.Series(effective, index=patients)
print("effective_series.head()\n")
print(effective_series.head())

patients = ["a", "b", "c", "d"]
columns = {
    "sys_initial": [120, 126, 130, 115],
    "dia_initial": [75, 85, 90, 87],
    "sys_final": [115, 123, 130, 118],
    "dia_final": [70, 82, 92, 87],
}
df = pd.DataFrame(columns, index=patients)

# same way
columns = {
    "sys_initial": pd.Series([120, 126, 130, 115], index=patients),
    "dia_initial": pd.Series([75, 85, 90, 87], index=patients),
    "sys_final": pd.Series([115, 123, 130, 118], index=[patients]),
    "dia_final": pd.Series([70, 82, 92, 87], index=patients),
}
df = pd.DataFrame(columns)
print(df.head())
