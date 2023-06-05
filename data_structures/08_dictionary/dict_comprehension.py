"""Dictionary Comprehension"""
import random

city_names = ["Paries", "London", "Berlin", "Madrid"]

city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)


above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}
print(above_25)
