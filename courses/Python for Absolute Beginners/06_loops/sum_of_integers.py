"""
Programming Challenge: Sum of Numbers From A Positive Integer
1. User input and assign in to a variable
2. Use a while loop to sum up numbers from the variable to 1
3. Print the user input value and print the sum from the while loop
"""

user_input = int(input("Enter an integer: "))
preserved_user_input = user_input
sum_up = 0
while user_input > 0:
    print(user_input)
    sum_up = sum_up + user_input
    user_input -= 1

print("The user input is " + str(preserved_user_input))
print("The sum of the while loop is " + str(sum_up))
