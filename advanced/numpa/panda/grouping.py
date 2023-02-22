"""
Database-style operations with Pandas
    - index operations in Pandas makes it suitable for database style manipulations
    - counting, joining, grouping and aggregations
    - Grouping, aggregations and transforms
      - pd.DataFrame.groupby
      - pd.DataFrame.agg
      - pd.DataFrame.transform
"""
import pandas as pd
import numpy as np

patients = ["a", "b", "c", "d", "e", "f"]

columns = {
    "sys_initial": [120, 126, 130, 115, 150, 117],
    "dia_initial": [75, 85, 90, 87, 90, 74],
    "sys_final": [115, 123, 130, 118, 130, 121],
    "dia_final": [70, 82, 92, 87, 85, 74],
    "drug_admst": [True, True, True, True, False, False],
}
df = pd.DataFrame(columns, index=patients)
print("df: ", df)


df.groupby("drug_admst")
for value, group in df.groupby("drug_admst"):
    print("Value: {}".format(value))
    print("Group DataFrame:")
    print(group)


# mean, max or standard deviation
# agg - aggregtations
mean = df.groupby("drug_admst").agg(np.mean)
print("mean: \n", mean)

max = df.groupby("drug_admst").agg(np.max)
print("max: \n", max)

std = df.groupby("drug_admst").agg(np.std)
print("std: \n", std)

# Intermediate steps for processing on the DataFrame groups that do not represent a
# summarization are called transforms.
# replace missing values with the average of the other values in the same group
df.loc["a", "sys_initial"] = None
df.loc["b", "dia_initial"] = None
df.loc["c", "sys_final"] = None
df.loc["d", "dia_final"] = None
transformed = df.groupby("drug_admst").transform(lambda df: df.fillna(df.mean()))
print("transform: \n", transformed.head())

transformed_mean = df.groupby("drug_admst").agg(np.mean)
print("transformed_mean: \n", transformed_mean)

transformed_max = df.groupby("drug_admst").agg(np.max)
print("transformed_max: \n", transformed_max)

transformed_std = df.groupby("drug_admst").agg(np.std)
print("transformed_std: \n", transformed_std)
