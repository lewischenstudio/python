"""
Do all of this in a .py file in Pycharm.
- create a variable and assign it a dictionary that has 5 key value pairs
- print and access the value held at the third key in the dictionary
- use the in keyword to check if a key appears in the dictionary and print the
  result
- use not in to check if a key does not appear in the dictionary and print the
  result
"""

furniture = {"chair": 1, "desk": 2, "lamp": 3, "table": 4, "bed": 5}
print(furniture["lamp"])
print("table" in furniture)
print("america flag" in furniture)
print("toilet" not in furniture)
print("computer" not in furniture)
