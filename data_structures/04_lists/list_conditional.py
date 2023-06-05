"""Conditional List Comprehension"""

prev_list = [-1, -10, -20, 2, -90, 60, 45, 20]
new_list = [number for number in prev_list if number > 0]
print(prev_list)
print(new_list)


sentence = "My name is Lewis"


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


prev_list = [-1, -10, -20, 2, -90, 60, 45, 20]
new_list = [number if number > 0 else "negative number" for number in prev_list]  # noqa
print(new_list)


def get_number(number):
    if number > 0:
        return number
    return "negative number"


new_list = [get_number(number) for number in prev_list]
print(new_list)
