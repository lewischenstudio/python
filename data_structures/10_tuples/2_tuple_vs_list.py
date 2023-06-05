"""
Tuples vs lists
- We generally use tuples for heterogenous (different) data types
  and lists for homogeneous (similar) data types
- Iterating through a tuple is faster than through list
- Tuples that contain immutable elements can be used as a key for a dictionary
- If you have data that doesn't change, implementing it as tuple will guarantee
  that it remains write-protected.
"""

list1 = [0, 1, 2, 3, 4, 5, 6, 7]

# list1 = [7,6,5,4,3,2,1]

del list1[0]

print(list1)

tuple1 = 0, 1, 2, 3, 4, 5, 6, 7

# del tuple1[0]

# print(tuple1)

"""
Methods that can NOT be used for tuples:
- append()
- insert()
- remove()
- pop()
- clear ()
- asort()
- reverse()
"""

list1 = [(1, 2), (9, 0), (3, 4)]
tuple1 = ([1, 2], [3, 4], [5, 6])

print(list1)
print(tuple1)
