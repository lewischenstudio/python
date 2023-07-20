"""List Comprehension"""

prev_list = [1, 2, 3]
new_list = []
for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)
print(new_list)
list_ = [i * 2 for i in prev_list]
print(list_)

language = "Python"
letter_list = [letter for letter in language]
print(letter_list)
