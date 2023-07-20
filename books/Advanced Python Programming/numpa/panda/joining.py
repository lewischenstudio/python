"""
Database-style operations with Pandas
    - index operations in Pandas makes it suitable for database style manipulations
    - counting, joining, grouping and aggregations
    - Joining
      - Useful to aggregate data that is scattered among different tables
      - pd.DataFrame.
"""
import pandas as pd


patients = ["a", "b", "c", "d", "e", "f"]

columns = {
    "sys_initial": [120, 126, 130, 115, 150, 117],
    "dia_initial": [75, 85, 90, 87, 90, 74],
    "sys_final": [115, 123, 130, 118, 130, 121],
    "dia_final": [70, 82, 92, 87, 85, 74],
    "drug_admst": [True, True, True, True, False, False],
}
df = pd.DataFrame(columns, index=patients)


# Include the location of the hospital for the data
# index: H1, H2, H3
# store in the hospital table
hospital_dict = {
    "name": ["City 1", "City 2", "City 3"],
    "address": ["Address 1", "Address 2", "Address 3"],
    "city": ["City 1", "City 2", "City 3"],
}
hospitals = pd.DataFrame(
    hospital_dict,
    index=["H1", "H2", "H3"],
)

hospital_id = ["H1", "H2", "H2", "H3", "H3", "H3"]
df["hospital_id"] = hospital_id
print("df: \n", df)

# Find the city where the measurement was taken for each patient
# map the keys from the hospital_id to the city stored in the hospitals table

# Find one city
city = hospitals.loc[(df.loc["a", "hospital_id"])].city
print("city: ", city)

# Find all cities with Python dictionary
hospital_dict = {
    "H1": ("City 1", "Name 1", "Address 1"),
    "H2": ("City 2", "Name 2", "Address 2"),
    "H3": ("City 3", "Name 3", "Address 3"),
}
cities = [hospital_dict[key][0] for key in hospital_id]
print("python cities: \n", cities)

# Find all cities with join
cities = hospitals.loc[hospital_id, "city"].values[:]
print("join cities: \n", cities)

# Join all columns
result = df.join(hospitals, on="hospital_id")
cities = result.columns
print("result cities: \n", cities)
