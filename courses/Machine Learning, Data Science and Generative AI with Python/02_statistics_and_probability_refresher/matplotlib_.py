"""Matplotlib"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from pylab import randn

x = np.arange(-3, 3, 0.01)

plt.plot(x, norm.pdf(x))
plt.show()

# Multiple Plots on One Graph
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

# Save it to a File
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig("MyPlot.png", format="png")

# Adjust the Axes
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

# Add a Grid
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
axes.grid()
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

# Change Line Types and Colors
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
axes.grid()
plt.plot(x, norm.pdf(x), "b-")
plt.plot(x, norm.pdf(x, 1.0, 0.5), "r:")
plt.show()

# Labeling Axes and Adding a Legend
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
axes.grid()
plt.xlabel("Greebles")
plt.ylabel("Probability")
plt.plot(x, norm.pdf(x), "b-")
plt.plot(x, norm.pdf(x, 1.0, 0.5), "r:")
plt.legend(["Sneetches", "Gacks"], loc=4)
plt.show()

# XKCD Style
plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate(
    "THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED",
    xy=(70, 1),
    arrowprops=dict(arrowstyle="->"),
    xytext=(15, -10),
)

plt.plot(data)

plt.xlabel("time")
plt.ylabel("my overall health")

# Pie Chart
# Remove XKCD mode:
plt.rcdefaults()

values = [12, 55, 4, 32, 14]
colors = ["r", "g", "b", "c", "m"]
explode = [0, 0, 0.2, 0, 0]
labels = ["India", "United States", "Russia", "China", "Europe"]
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title("Student Locations")
plt.show()

# Bar Chart
values = [12, 55, 4, 32, 14]
colors = ["r", "g", "b", "c", "m"]
plt.bar(range(0, 5), values, color=colors)
plt.show()

# Scatter Plot
X = randn(500)
Y = randn(500)
plt.scatter(X, Y)
plt.show()

# Histogram
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()

# Box & Whisker Plot

# Useful for visualizing the spread & skew of data.
# The red line represents the median of the data, and the box represents the
# bounds of the 1st and 3rd quartiles.
# So, half of the data exists within the box.
# The dotted-line "whiskers" indicate the range of the data - except for
# outliers, which are plotted outside the whiskers. Outliers are 1.5X or more
# the interquartile range. This example below creates uniformly distributed
# random numbers between -40 and 60,
# plus a few outliers above 100 and below -100:

uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()


# Activity

# Try creating a scatter plot representing random data on age vs. time spent
# watching TV. Label the axes.
X = np.random.uniform(low=1, high=120, size=(100,))
Y = np.random.uniform(low=1, high=12, size=(100,))
plt.scatter(X, Y)
plt.xlabel("Age")
plt.ylabel("Time Spent Watching TV")
plt.show()
