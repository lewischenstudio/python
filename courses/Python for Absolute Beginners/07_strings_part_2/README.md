## Section 07: Strings Part 2

#### Table of Contents

- string methods 1
- string methods 1 exercises
- string methods 1 exercise solutions
- string methods 2
- string methods 2 exercises
- string methods 2 exercise solutions
- len()
- Programming Challenge: String Reverser
- String Reverser Solution
- Programming Challenge: Word Counter
- Word Counter Solution
- .format()

### string methods 1

|    Methods     |                 Description                 |
| :------------: | :-----------------------------------------: |
|   `upper()`    |            Return upper letters             |
|   `lower()`    |            Return lower letters             |
|  `isupper()`   |       Check if string is upper letter       |
|  `islower()`   |       Check if string is lower letter       |
|  `.isalpha()`  |      Check string if only has letters       |
|  `.isalnum()`  | Check if string has all numbers and letters |
| `isdecimal()`  |      Check if string has only numbers       |
|  `isspace()`   |         Check if string has spaces          |
|  `istitle()`   |       Check if string has title case        |
| `startswith()` |    Check if string starts with substring    |
| `.endswith()`  |     Check if string ends with substring     |
|    `join()`    | Turn array of strings into a single string  |
|   `split()`    |   Split a string into an array of strings   |

### string methods 1 exercises

Do all of this in a .py file in Pycharm:

1. Create a variable called mixed_case and assign it the string "A Song of Ice
   and Fire"
2. Use `.isupper()` to check if mixed_case is a string of all upper case
   letters. print() the result.
3. Use `.islower()` to check if mixed_case is a string of all lower case
   letters. print() the result.
4. Change all of the letters in mixed_case to upper case letters using
   `.upper()` and print() the result.
5. Change all of the letters in mixed_case to lower case letters using
   `.lower()` and print() the result.
6. Use the `.istitle()` method to check if mixed_case is title case and print
   the result.
7. Create a variable called title_case and assign it the result of `.title()`
   being called on mixed_case.
8. print() title_case
9. Call `startswith()` on mixed_case with the letter mixed_case starts with as
   its argument. print() the result.
10. Call `endswith()` on mixed_case with the letter mixed_case ends with as its
    argument. print() the result.
11. Create a variable called words and assign it the result of `split()` being
    used on mixed_case.
12. print the variable "words".
13. Use the `.join()` method to join together all of the items in the list
    assigned to words as a single string. Use `.isalpha()` to check if the
    string is made up entirely of letters. Finally, use print() to display the
    result.

### string methods 1 exercise solutions

```python
mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
words = mixed_case.split()
print(words)
print("".join(words).isalpha())
```

### string methods 2

|   Methods   |                                           Description                                            |
| :---------: | :----------------------------------------------------------------------------------------------: |
|  `rjust()`  |          Adds spaces or character(s) to the left and make the string with given length           |
|  `ljust()`  |          Adds spaces or character(s) to the right and make the string with given length          |
| `center()`  | Adds spaces or character(s) to both the left and the right and make the string with given length |
|  `strip()`  |                 Remove white spaces or character(s) from both side of the string                 |
| `lstrip()`  |                 Remove white spaces or character(s) from left side of the string                 |
| `rstrip()`  |                Remove white spaces or character(s) from right side of the string                 |
| `replace()` |                 Replace the first argument with the second argument in a string                  |

```python
print("hello world".rjust(15, "*")) # ****hello world
print("hello world".ljust(15, "*")) # hello world****
print("hello world".center(15, "*")) # **hello world**
```

```python
print("hello world1111".strip("1")) # hello world
print("hello world1111".rstrip("1")) # hello world
print("hello world1111".lstrip("1")) # hello world1111
```

```python
print("Good morning".replace("morning", "afternoon")) # Good afternoon
```

### string methods 2 exercises

Do all of this in a .py file:

- Create a variable called the_string and assign it the string "North Dakota".
- Call `.rjust()` on the_string with 17 as its argument and print() the result.
- Call `.ljust()` on the_string with the arguments 17 and "\*" then print() the
  result.
- Create a variable called center_plus and assign it the result of .center()
  being called on the_string with 16 and "+" as arguments.
- Use `print()` to display the string assigned to center_plus.
- Call `.lstrip()` on the_string to remove "North" then print() the result.
- Call `.rstrip()` on center_plus with "+" as its argument and print() the
  result.
- Call `.strip()` on center_plus with "+" as its argument and print() the
  result.
- Call `.replace()` on the_string and replace "North" with "South". print() the
  result.

### string methods 2 exercise solutions

```python
the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))
```

### len()

Print the length of a given string

```python
print(len("tree")) # 4
```

### Programming Challenge: String Reverser

For this challenge, you will be writing a program which uses a for loop to
reverse a string.

Start by creating a variable and assigning it a string as user input using
input().

Use a for loop to reverse the string. You will need to use range with all 3
inputs for this. In addition, you should create a variable before the for loop
and assign it an empty string. The variable will be reassigned multiple times
within the for loop and end up holding the new reversed string.

Print the reversed string at the bottom of your program.

### String Reverser Solution

```python
user_string = input("Please enter a string.")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)
```

### Programming Challenge: Word Counter

For this programming challenge, write a function in a .py file which takes 1
string as an argument, finds out the number of words in that string, then
returns that number.

For example, if the program was used on the string "This is a string.", then the
function would return 4.

Assumptions:

- Assume that the string will be assigned to a variable and that it will contain
  at least 1 word.
- Assume that there will never be 2 or more consecutive spaces in a row within
  the string.
- Contractions and possessive words with an apostrophe like "it's" or "Brian's"
  count as 1 word.
- Hyphenated words like "ice-cream" count as 1 word.
- Numbers in the string such as the "007" in "James Bond is 007." count as words
- There will be no double quotes "" within in the string.

Hints for this problem:

1. Use string methods to filter out characters besides numbers, letters, spaces,
   apostrophes, and hyphens.
2. Count the number of spaces in the filtered string and add 1 to that since the
   string will always contain at least 1 word. This will give you the number of
   words it contains.

You should test your program with many different strings.

However, the strings that the solution code is being used on are the 3 strings
below.

```python
str_1 = "James Bond is 007." str_2 = "When the moon hits your eye like a big
pizza pie, that's amore!" str_3 = "Anyway, like I was sayin', shrimp is the
fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried,
stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew,
shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
```

So, for your final solution, copy the above into your .py file and print() 3
calls of your function, once for each of the 3 variables above.

### Word Counter Solution

```python
str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."


# This function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, and assigns that string to
# the variable spaces_and_letters so that the number of words in it can by found by counting spaces between words.
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count


print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))
```

### .format()

```python
name = input("What is the job applicant's name?")
degree = input("What is their major at college?")
job = input("What is their current occupation?")
experience = input("How many years have they been working in their field?")

print(name + "majored in " + degree + ", works as a " + job + ", and has  " + experience + " years of experience.")
```

#### .format()

```python
print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))
```
