"""
create two variables, one which will hold a randomly generated integer between 10 and 25 
(inclusive of both 10 and 25), and another which will hold a randomly generated integer 
between and inclusive of 200 and 400. The first variable represents the number of gallons 
of gas that the car's fuel tank holds. The second variable represents the miles that the 
car can travel on a full tank before needing a refuel.

Using the formula miles per gallon (MPG) = miles driven/gallons used, calculate the car's 
MPG and display it in the output using print().  Use floor division instead of regular 
division for this calculation to get an integer instead of a float.  This will give a 
realistic approximation of miles per gallon even though floats such as 19.8 round down a 
large amount when using floor division since sometimes, car manufacturers sometimes 
exaggerate miles per gallon. 
"""
from random import randint

gallons = randint(10, 25)
miles = randint(200, 400)

print(miles)
print(gallons)
print(miles // gallons)
