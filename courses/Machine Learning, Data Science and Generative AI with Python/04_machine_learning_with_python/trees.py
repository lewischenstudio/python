"""Decision Trees: Predicting Hiring Decisions"""

import os
import pandas as pd
import pydotplus
from six import StringIO
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from IPython.display import Image
from predict_message import predict_message


input_file = os.path.join(os.getcwd(), "PastHires.csv")
df = pd.read_csv(input_file, header=0)

print(df.head())

# scikit-learn needs everything to be numerical for decision trees to work.
# So, we'll map Y,N to 1,0 and levels of education to some scale of 0-2. In
# the real world, you'd need to think about how to deal with unexpected or
# missing data! By using map(), we know we'll get NaN for unexpected values.
d = {"Y": 1, "N": 0}
df["Hired"] = df["Hired"].map(d)
df["Employed?"] = df["Employed?"].map(d)
df["Top-tier school"] = df["Top-tier school"].map(d)
df["Interned"] = df["Interned"].map(d)
d = {"BS": 0, "MS": 1, "PhD": 2}
df["Level of Education"] = df["Level of Education"].map(d)
print(df.head())


# Next we need to separate the features from the target column that we're
# trying to bulid a decision tree for.
features = list(df.columns[:6])
print(features)

# Now actually construct the decision tree:
y = df["Hired"]
X = df[features].values
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Plot the tree
tree.plot_tree(clf)
# plt.show()


# Plot the tree using GraphViz
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data, feature_names=features)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())


# Predict employment for the following attributes
predicts = [10, 1, 4, 0, 0, 0]
predict_message(
    "Decision Tree Classifier",
    features,
    predicts,
    clf.predict([predicts])[0],
)

predicts = [3, 1, 2, 2, 0, 0]
predict_message(
    "Decision Tree Classifier",
    features,
    predicts,
    clf.predict([predicts])[0],
)

# Ensemble learning: using a random forest
# We'll use a random forest of 10 decision trees to predict employment of
# specific candidate profiles:
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)

# Predict employment of an employed 10-year veteran
predict_message(
    "Random Forest Classifier",
    features,
    predicts,
    clf.predict([predicts])[0],
)

# ...and an unemployed 10-year veteran
predicts = [10, 0, 4, 0, 0, 0]
predict_message(
    "Random Forest Classifier",
    features,
    predicts,
    clf.predict([predicts])[0],
)
