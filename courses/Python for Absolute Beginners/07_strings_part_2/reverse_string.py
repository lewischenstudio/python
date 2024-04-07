"""
For this challenge, you will be writing a program which uses a for loop to reverse a string. 

Create a variable and assign it to a user input using input().

Create another variable and assign in as an empty string.

Use a for loop to reverse the string. You will need to use range() with all 3 parameters for this.
The variable above will be reassigned multiple times within the for loop and end up holding the new 
reversed string.

Print the reversed string at the bottom of your program.
"""

user_input = input("Enter your string: ")

reverse_string = ""

# the for loop in the reverse direction
# example: user_input = "abcde"
# example: range(4, -1, -1)
for index in range(len(user_input)-1, -1, -1):
    # print each character in user_input in reverse direction
    reverse_string += user_input[index]

print(reverse_string)