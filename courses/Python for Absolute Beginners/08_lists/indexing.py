"""
Do all of this in a .py file in Pycharm.

1. Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
2. Access the first list from the list of lists in step 1 by index then
   print it.
3. Access the 14 from the list in step 1 then print it.
4. Create a second variable and assign it the list ["chair", "table", "desk",
   "lamp", "bed"]
5. Use a negative integer to access "chair" from the variable in step 4 by
   index then print it.
6. Print "Most people own at least 2 chairs." by concatenating the 2 from the
   list in step 1 and the "chair" from the list in step 4 with "Most people own
   at least ", a space, and a period.
7. Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
8. Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
9. Print the slice [8.76, 6.54] from the variable you created in step 7.
10. Print the slice [0.98, 8.76] from the variable you created in step 7.
"""

number_list = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(number_list[0])
print(number_list[3][1])
furniture_list = ["chair", "table", "desk", "lamp", "bed"]
print(furniture_list[-5])
print(
    "Most people own at least "
    + str(number_list[0][1])
    + " "
    + furniture_list[-5]
    + "s."
)
float_list = [0.98, 8.76, 6.54, 4.32]
print(float_list[1:4])
print(float_list[1:3])
print(float_list[:2])
# Refresher
# my_list = [0, 1, "ok", [10, 9]]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])  # [10, 9]
# print(my_list[3][0])
# print(my_list[3][1])

# this_list = [[1], [2, 3, [4]]]
# print(this_list)
# print(this_list[0])  # [1]
# print(this_list[0][0])  # 1
# print(this_list[1])  # [2, 3, [4]]
# print(this_list[1][0])  # 2
# print(this_list[1][1])  # 3
# print(this_list[1][2])  # [4]
# print(this_list[1][2][0])  # 4
