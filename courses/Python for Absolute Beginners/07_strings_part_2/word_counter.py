"""
Word Counter
"""

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

def word_counter(text):
    # return the number of words in a string
    counter = 0
    text_list = text.split(" ")
    for word in text_list:
        counter += 1
    return counter

print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))