"""
Indexing Series and DataFrame objects
    - loc
    - iloc
    - pd.Series.sort_index
"""
import pandas as pd


# DateFrame
patients = ["a", "b", "c", "d"]
effective = [True, True, False, False]
effective_series = pd.Series(effective, index=patients)

# loc: retrieve data by its key
effective_series.loc["a"]

# iloc: retrieve data by its position (index)
effective_series.iloc[0]

# mixed of the above
effective_series["a"]  # By key
effective_series.get(0)  # By position

columns = {
    "sys_initial": pd.Series([120, 126, 130, 115], index=patients),
    "dia_initial": pd.Series([75, 85, 90, 87], index=patients),
    "sys_final": pd.Series([115, 123, 130, 118], index=patients),
    "dia_final": pd.Series([70, 82, 92, 87], index=patients),
}
df = pd.DataFrame(columns)

df.loc["a"]
df.iloc[0]

# The loc attribute will index both row and column by key
# The iloc version will index row and column by an integer
df.loc["a", "sys_initial"]  # is equivalent to
df.loc["a"].loc["sys_initial"]

df.iloc[0, 1]  # is equivalent to
df.iloc[0].iloc[1]

# Retrieve column by name
df["sys_initial"]  # is equivalent to
df.sys_initial

# Retrieve column by position
df[df.columns[2]]  # is equivalent to
df.iloc[:, 2]


# Sort the index for binary search:
# Create a series with duplicate index
index = list(range(1000)) + list(range(1000))

# Accessing a normal series is a O(N) operation
series = pd.Series(range(2000), index=index)

# Sorting will improve lock-up scaling to O(log(N))
series.sort_index(inplace=True)
print(series.loc[0])
