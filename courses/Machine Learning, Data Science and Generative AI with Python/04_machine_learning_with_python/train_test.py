"""Using Train/Test to Prevent Overfitting a Polynomial Regression"""

import matplotlib.pyplot as plt
import numpy as np
from pylab import scatter
from sklearn.metrics import r2_score

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds


scatter(pageSpeeds, purchaseAmount)


# Now we'll split the data in two - 80% of it will be used for "training" our
# model, and the other 20% for testing it. This way we can avoid overfitting.
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

# Our trainig dataset
scatter(trainX, trainY)


# Our test dataset
scatter(testX, testY)


# Now we'll try to fit an 8th-degree polynomial to this data (which is almost
# certainly overfitting, given what we know about how it was generated!)
# Let's plot our polynomial against the training data:
train_x = np.array(trainX)
train_y = np.array(trainY)
p4 = np.poly1d(np.polyfit(train_x, train_y, 8))

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(train_x, train_y)
plt.plot(xp, p4(xp), c="r")
plt.show()

# Let's plot our polynomial against the test data:
test_x = np.array(testX)
test_y = np.array(testY)

axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(test_x, test_y)
plt.plot(xp, p4(xp), c="r")
plt.show()


# the r-squared score on the test data is kind of horrible
# This tells us that our model isn't all that great
r2 = r2_score(test_y, p4(test_x))
print(r2)
# 0.3001816861144364

# It fits the training data better, but the score is still far from optimal
r2 = r2_score(np.array(trainY), p4(np.array(trainX)))
print(r2)
# 0.6427069514693098
