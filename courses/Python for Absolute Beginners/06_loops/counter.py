# counter = 0
# while counter < 3:
#     print("counter = " + str(counter) + " and print something for " + str(counter))
#     counter += 1
#     print('after counter +=1, counter = ' + str(counter))
# print('after the while loop, counter = ' + str(counter))

# counter = 0
# if counter < 3:
#     print("counter = " + str(counter) + " and print something for " + str(counter))
#     counter += 1
#     print('after counter +=1, counter = ' + str(counter))
# if counter < 3:
#     print("counter = " + str(counter) + " and print something for " + str(counter))
#     counter += 1
#     print('after counter +=1, counter = ' + str(counter))
# if counter < 3:
#     print("counter = " + str(counter) + " and print something for " + str(counter))
#     counter += 1
#     print('after counter +=1, counter = ' + str(counter))
# print('after the while loop, counter = ' + str(counter))

# Infinite Loop 1: counter += 0
counter = 0
while counter < 3:
    print("counter = " + str(counter) + " and print something for " + str(counter))
    # counter += 0
    print('after counter += 0, counter = ' + str(counter))
print('after the while loop, counter = ' + str(counter))

# Infinite Loop 2: while counter >= 0
counter = 0
while counter >= 0:
    print("counter = " + str(counter) + " and print something for " + str(counter))
    counter += 1
    print('after counter +=1, counter = ' + str(counter))
print('after the while loop, counter = ' + str(counter))