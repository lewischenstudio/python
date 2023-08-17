"""Conditional Probability

We want to know how much stuff people purchase given their age range.
It generates 100,000 random "people" and randomly assigns them as being
in their 20's, 30's, 40's, 50's, 60's, or 70's.
"totals" contains the total number of people in each age group.
"purchases" contains the total number of things purchased by people in
each age group. The grand total of purchases is in totalPurchases, and
we know the total number of people is 100,000.
"""

from numpy import random

random.seed(0)

totals = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
purchases = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
totalPurchases = 0
totalPopulation = 100000
for _ in range(totalPopulation):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade) / 100.0
    totals[ageDecade] += 1
    if random.random() < purchaseProbability:
        totalPurchases += 1
        purchases[ageDecade] += 1

print("totals: ", totals)
print("purchases: ", purchases)
print("totalPurchases: ", totalPurchases)


# Conditional probability
# First let's compute P(E|F) = P(E,F) / P(F)
# where E is "purchase" and F is "you're in your 30's".
# P(E,F) would be the probability of both being in your 30's and buying
# something, out of the total population.
# P(F) is just the probability of being 30 in this data set
# The probability of someone in their 30's buying something is just the
# percentage of how many 30-year-olds bought something
PENF = float(purchases[30]) / totalPopulation
PF = float(totals[30]) / totalPopulation
PEF = PENF / PF  # same as float(purchases[30]) / float(totals[30])
print("P(purchase | 30s): " + str(PEF))


# P(F) is just the probability of being 30 in this data set
PF = float(totals[30]) / totalPopulation
print("P(30's): " + str(PF))


# P(E) is the overall probability of buying something, regardless of your age
PE = float(totalPurchases) / totalPopulation
print("P(Purchase): " + str(PE))

# If E and F were independent, then we would expect P(E | F) to be about the
# same as P(E). But they're not; P(E) is 0.45, and P(E|F) is 0.3. So, that
# tells us that E and F are dependent (which we know they are in this example.)

# P(E,F) is different from P(E|F). P(E,F) would be the probability of both
# being in your 30's and buying something, out of the total population - not
# just the population of people in their 30's:
print("P(30's, Purchase): " + str(PENF))


# Let's also compute P(E)P(F), the product of P(E) and P(F)
# Something you may learn in stats is that P(E,F) = P(E)P(F), but this assumes
# E and F are independent. We've found here that P(E,F) is about 0.05, while
# P(E)P(F) is about 0.075. So when E and F are dependent - and we have a
# conditional probability going on - we can't just say that P(E,F) = P(E)P(F).
print("P(30's)P(Purchase): " + str(PE * PF))


# We can also check that P(E|F) = P(E,F)/P(F)
print(PENF / PF)


# Activity
# Modify the code above such that the purchase probability does NOT vary with
# age, making E and F actually independent. Then, confirm that P(E|F) is about
# the same as P(E), showing that the conditional probability of purchase for a
# given age is not any different than the a-priori probability of purchase
# regardless of age.
totals = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
purchases = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
totalPurchases = 0
totalPopulation = 100000
for _ in range(totalPopulation):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = 0.4
    totals[ageDecade] += 1
    if random.random() < purchaseProbability:
        totalPurchases += 1
        purchases[ageDecade] += 1

PE = float(totalPurchases) / totalPopulation
PEF = float(purchases[30]) / float(totals[30])
print("P(E): ", PE)
print("P(E|F): ", PEF)
