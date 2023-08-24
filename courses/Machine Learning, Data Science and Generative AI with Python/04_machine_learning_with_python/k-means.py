"""Clustering people based on income and age"""

import matplotlib.pyplot as plt
from numpy import random, array
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale


# Create fake income/age clusters for N people in k clusters
def createClusteredData(
    N: int,
    k: float,
    income_low: float,
    income_high: float,
    income_scale: float,
    age_low: float,
    age_high: float,
    age_scale: float,
):
    random.seed(10)
    pointsPerCluster = float(N) / k
    X = []
    for i in range(k):
        incomeCentroid = random.uniform(income_low, income_high)
        ageCentroid = random.uniform(age_low, age_high)
        for j in range(int(pointsPerCluster)):
            X.append(
                [
                    random.normal(incomeCentroid, income_scale),
                    random.normal(ageCentroid, age_scale),
                ]
            )
    X = array(X)
    return X


N_people = 100
k_clusters = 5
income_low = 20000.0
income_high = 200000.0
income_scale = 10000.0
age_low = 20.0
age_high = 70.0
age_scale = 2.0

data = createClusteredData(
    N_people,
    k_clusters,
    income_low,
    income_high,
    income_scale,
    age_low,
    age_high,
    age_scale,
)

model = KMeans(n_init=10, n_clusters=k_clusters)

# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# We can look at the clusters each data point was assigned to
print(model.labels_)

# Coordinates of cluster centers
print(model.cluster_centers_)

# Sum of squared distances of samples to their closest cluster center,
# weighted by the sample weights if provided.
print(model.inertia_)

# And we'll visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=model.labels_.astype(float))
plt.show()


# Activity
# Things to play with: what happens if you don't scale the data? What happens
# if you choose different values of K? In the real world, you won't know the
# "right" value of K to start with - you'll need to converge on it yourself.
# We are trying to get minimum model.inertia_ from the array of inertia by
# fitting the model to the data for k ranges from 3 to 10
inertia = []
for i in range(2, 11):
    k_clusters = i
    data = createClusteredData(
        N_people,
        k_clusters,
        income_low,
        income_high,
        income_scale,
        age_low,
        age_high,
        age_scale,
    )
    model = KMeans(n_init=10, n_clusters=k_clusters)
    model = model.fit(scale(data))
    inertia.append({"k": i, "value": model.inertia_})

print("inertia: \n", inertia)

# Obtain the minimum inertia
inertia.sort(key=lambda x: x["value"])
min_inertia = inertia[0]
min_k = min_inertia["k"]
print("min_k: ", min_k)


# Plot the data for k = int(min_inertia)
data = createClusteredData(
    N_people,
    min_k,
    income_low,
    income_high,
    income_scale,
    age_low,
    age_high,
    age_scale,
)
model = KMeans(n_init=10, n_clusters=k_clusters)
model = model.fit(scale(data))
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=model.labels_.astype(float))
plt.title(f"Clustering people based on income and age for k = {min_k}")
plt.ylabel("Age")
plt.xlabel("Income")
plt.show()
