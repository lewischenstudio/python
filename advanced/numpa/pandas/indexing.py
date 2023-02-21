"""
Indexing Series and DataFrame objects
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

# ix: mixed of the above
effective_series.ix["a"]  # By key
effective_series.ix[0]  # By position

# Equivalent
effective_series["a"]  # By key
effective_series[0]  # By position
