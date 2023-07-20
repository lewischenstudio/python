"""
1. Calculate Average Temperature
2. Find the Days Above Average Temperature
"""

num_days = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(1, num_days + 1):
    next_day = int(input("Day " + str(i) + "'s high temperature: "))
    temp.append(next_day)
    total += next_day

avg = round(total / num_days, 2)
print("\nAverage temperature = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day(s) above average")
