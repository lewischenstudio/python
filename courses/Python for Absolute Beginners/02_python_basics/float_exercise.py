"""
Programming Challenge: Grocery Store Purchase
A customer of a grocery store is purchasing 6 items. The names and prices of 
the items are as follows:

- Penne 16 oz Pack of 12 - $16.68
- Arrabiata Pasta Sauce 24 oz - $6.98
- Bag of 20 Organic Garlic Cloves - $16.78
- Italian Seasoning 1.5 oz Bottle - $15.26
- Artisan Baguettes Twin Pack - $3.00
- 12 oz Bag of Meatballs - $4.39

In a .py file, write a program which calculates the subtotal of all 6 
of these items using an expression.  The subtotal is just the sum of all 
of their prices.

Use print() to display the result of the expression.
"""

sub_total = 16.68 + 6.98 + 16.78 + 15.26 + 3 + 4.39
print(sub_total)
print(round(sub_total, 2))

# Solution 1

# Variables holding the prices of the six items:
 
# All of the variables were multiplied by 100 to make them into integers so that there would be no approximation errors
# when they were added together.
 
pasta = 16.68 * 100  # penne 16 oz, pack of 12
sauce = 6.98 * 100  # Arrabiata sauce 24oz
garlic = 16.78 * 100  # 20 pack garlic clove
seasoning = 15.26 * 100  # Italian Seasoning
bread = 3.00 * 100  # Baguette twin pack
meatballs = 4.39 * 100  # 12 oz bag of meatballs
# subtotal is the sum of all prices before any sales taxes or discounts are added
subtotal = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal)

# Solution 2
# Variables holding the prices of the six items:
 
pasta = 16.68  # penne 16 oz, pack of 12
sauce = 6.98  # Arrabiata sauce 24oz
garlic = 16.78  # 20 pack garlic clove
seasoning = 15.26  # Italian Seasoning
bread = 3.00  # Baguette twin pack
meatballs = 4.39  # 12 oz bag of meatballs
# A subtotal is the sum of all prices before any sales taxes or discounts are added.
 
# round() was used to round the subtotal to 2 decimal places since the sum of any amount of numbers that all have 2 
# numbers after the decimal will always have 2 numbers after its decimal point.
subtotal = round((pasta + sauce + garlic + seasoning + bread + meatballs), 2)
print(subtotal)