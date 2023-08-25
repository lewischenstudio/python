"""
XGBoost

Let's experiment using the Iris data set. This data set includes the width and
length of the petals and sepals of many Iris flowers, and the specific species
of Iris the flower belongs to. Our challenge is to predict the species of a
flower sample just based on the sizes of its petals. We'll revisit this data
set later when we talk about principal component analysis too.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb


iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))  # classes of sample to be classified
print("iris.data: \n", iris.data)
print("iris.target: \n", iris.target)
print(
    "size of data is {} and size of target is {}".format(
        len(iris.data),
        len(iris.target),
    )
)

# Let's divide our data into 20% reserved for testing our model, and the
# remaining 80% to train it with.
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=0
)


# Convert our data into the DMatrix format it expects -- one for the training
# data and one for the test data.
train = xgb.DMatrix(X_train, label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

# We'll define our hyperparameters. We're choosing softmax since this is a
# multiple classification problem, but the other parameters should ideally
# be tuned through experimentation.
param = {
    "max_depth": 4,
    "eta": 0.3,
    "objective": "multi:softmax",
    "num_class": 3,
}
epochs = 10

# Train the data with parameters
model = xgb.train(param, train, epochs)


predictions = model.predict(test)
print(predictions)


# Let's measure the accuracy on the test data...
accuracy = accuracy_score(y_test, predictions)
print("accuracy: ", accuracy)
