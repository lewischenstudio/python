"""
Programming Challenge: Find The Number of Characters in A String
1. User input and assign it to a variable
2. Use the for loop to sum up the number of characters in the variable
3. Print both the characters entered and the length of the characters
"""

user_input = input("Enter a word: ")
counter = 0
for letter in user_input:
    counter += 1

print("The user input is \"" + user_input + "\"")
print("The number of characters is " + str(counter))