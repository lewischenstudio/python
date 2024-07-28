"""Support Vector Classification"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm


# Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    np.random.seed(1234)
    pointsPerCluster = float(N) / k
    X = []
    y = []
    for i in range(k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append(
                [
                    np.random.normal(incomeCentroid, 10000.0),
                    np.random.normal(ageCentroid, 2.0),
                ]
            )
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y


(X, y) = createClusteredData(100, 5)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y.astype(float))
plt.show()

scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X)
X = scaling.transform(X)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y.astype(float))
plt.show()


# We'll use linear SVC to partition our graph into clusters
C = 1.0
kernel = "linear"
svc = svm.SVC(kernel=kernel, C=C).fit(X, y)


# By setting up a dense mesh of points in the grid and classifying all of them,
# we can render the regions of each cluster as distinct colors:
def plotPredictions(clf, kernel):
    # Create a dense grid of points to sample
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.001), np.arange(-1, 1, 0.001))

    # Convert to Numpy arrays
    npx = xx.ravel()
    npy = yy.ravel()

    # Convert to a list of 2D (income, age) points
    samplePoints = np.c_[npx, npy]

    # Generate predicted labels (cluster numbers) for each point
    Z = clf.predict(samplePoints)

    plt.figure(figsize=(8, 6))
    Z = Z.reshape(xx.shape)  # Reshape results to match xx dimension
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)  # Draw the contour
    plt.scatter(X[:, 0], X[:, 1], c=y.astype(float))  # Draw the points
    plt.title(f"Kernel = {kernel}")
    plt.show()


plotPredictions(svc, kernel)


# Predict for a given point:
print(svc.predict(scaling.transform([[200000, 40]])))

print(svc.predict(scaling.transform([[50000, 65]])))


# Activity
# "Linear" is one of many kernels scikit-learn supports on SVC. Look up the
# documentation for scikit-learn online to find out what the other possible
# kernel options are. Do any of them work well for this data set?

# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
# kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable,
# Specifies the kernel type to be used in the algorithm. If none is given,
# ‘rbf’ will be used. If a callable is given it is used to pre-compute the
# kernel matrix from data matrices; that matrix should be an array of shape
# (n_samples, n_samples).
kernels = ["poly", "rbf", "sigmoid", "precomputed"]
for kernel in kernels:
    C = 1.0
    svc = svm.SVC(kernel="linear", C=C).fit(X, y)
    plotPredictions(svc, kernel)
    print(f"Prediction for kernel = {kernel} \n")
    print(svc.predict(scaling.transform([[200000, 40]])))
    print(svc.predict(scaling.transform([[50000, 65]])))

# Result: they work well for this data set
