"""
List Exercise
1. Create a variable and assign it a list that contains an integer, a float, a
   Boolean value, a string, and a list of 3 integers.
2. Create another variable and assign it a call of the list() function with a
   string as its argument.
3. Use the keyword "in" to check if the letter "e" is in the list assigned to
   the variable from step 2 and print the result.
4. Use the keyword "not in" to check if the letter "a" is not in the list
   assigned to the variable from step 2 and print the result.
"""

list_1 = [1, 2.1, False, "abc", [1, 2, 3,]]

list_2 = list("jjj")

print("e" in list_2)

print("a" not in list_2)