"""Seaborn"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

file_path = os.path.join(os.getcwd(), "FuelEfficiency.csv")

df = pd.read_csv(file_path)

gear_counts = df["# Gears"].value_counts()

gear_counts.plot(kind="bar")


# Seaborn
sns.set()

gear_counts.plot(kind="bar")


df.head()

# "distplot" can be used to plot a histogram together with a smooth
# distribution of that histogram overlaid on it.
sns.distplot(df["CombMPG"])


# "pair plot" lets you visualize plots of every combination of
# various attributes together, so you can look for interesting
# patterns between features.
df2 = df[["Cylinders", "CityMPG", "HwyMPG", "CombMPG"]]
df2.head()

# Seaborn currently has a bug with the hue parameter so we've omitted it
# By studying the results above, you can see there is a relationship
# between number of cylinders and MPG, but MPG for 4-cylinder vehicles
# ranges really widely. There also appears to be a good linear relationship
# between the different ways of measuring MPG values, until you get into
# the higher MPG ratings.
sns.pairplot(df2, hue="Cylinders", height=2.5)


# "scatterplot" plots individual data points across two axes of your choosing,
# so you can see how your data is distributed across those dimensions.
sns.scatterplot(x="Eng Displ", y="CombMPG", data=df)


#  "jointplot", which combines a scatterplot with histograms on both axes.
# This lets you visualize both the individual data points and the distribution
# across both dimensions at the same time.
sns.jointplot(x="Eng Displ", y="CombMPG", data=df)

# The "lmplot" is a scatterplot, but with a linear regression line computed and
# overlaid onto the data.
sns.lmplot(x="Eng Displ", y="CombMPG", data=df)


# "box plot." is "box and whiskers" plot, which is useful for visualizing
# typical values for a given category without getting distracted by outliers.
# Each box represents the range between the first and third quartiles of the
# data, with a line representing the median value. The "whiskers" that extend
# from the box represent the spread of the remainder of the data, apart from
# clear outliers that are plotted as individual points outside of the whiskers.
sns.set(rc={"figure.figsize": (15, 5)})
ax = sns.boxplot(x="Mfr Name", y="CombMPG", data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)


# "swarm plot." plots each individual data point - but does so in such way
# that groups them together based on their distribution.
ax = sns.swarmplot(x="Mfr Name", y="CombMPG", data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)


# "count plot." This is basically the same thing as a histogram, but for
# categorical data. It lets you count up how many times each given category
# on the X axis occurs in your data, and plot it.
ax = sns.countplot(x="Mfr Name", data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

#  A heat map allows you to plot tabular, 2D data of some sort, with colors
# representing the individual values in each cell of the 2D table.

# In this example, we'll create a pivot table from our original dataframe,
# to create a 2D table that contains the average MPG ratings for every
# combination of number of cylinders and engine displacement.

# The resulting heatmap shows all of the engine displacement values along the
# X axis, and all of the cylinder values along the Y axis. For each cell of
# the table, the actual average MPG rating for that combination of cylinders
# and engine displacement is represented not as a number, but as a color that
# ranges from dark for small values, and light for larger values.

# And, this does allow you visualize a clear trend where things get
# progressively darker as we move from the top-left of the graph to the
# bottom-right. Which makes sense; higher MPG ratings are associated with
# lower numbers of cylinders, and lower engine displacment values. By the time
# we get to an 8-liter 16-cylinder engine, the average MPG is at its worst of
# about 12, represented by the color black.

# This particular graph has a lot of missing data, but the heatmap deals with
# that gracefully. A 3-cylinder 8-liter engine simply does not exist!
df2 = df.pivot_table(
    index="Cylinders",
    columns="Eng Displ",
    values="CombMPG",
    aggfunc="mean",
)
sns.heatmap(df2)


# Exercise
# Explore the relationship between the number of gears a car has, and its
# combined MPG rating. Visualize these two dimensions using a scatter plot,
# lmplot, jointplot, boxplot, and swarmplot. What conclusions can you draw?

# scatterplot
# A scatterplot arranges itself into columns when you have ordinal data like
# the number of gears, but it tells us that there's a pretty wide range of
# MPG values for each type of gear box, although if you look at where the
# data points are clustered, you can sort of see a downward trend in MPG as
# the number of gears increases. But it's subtle. We also see that there's
# such a thing as a single gear car. These are "continuously variable
# transmission" cars, and we can see they typically have high MPG ratings
# and are therefore quite efficient.
sns.scatterplot(x="# Gears", y="CombMPG", data=df)


# lmplot
# The "lmplot" gives us a linear regression of our data overlaid on the graph,
# and this makes the overall trend of lower MPG's with more gears apparent.
# More gears isn't better when it comes to efficiency, it seems. We also see
# the error bars on that regression line, which tells us this trend is probably
# real and not just the result of randomness in the samples.
sns.lmplot(x="# Gears", y="CombMPG", data=df)


# jointplot
# The jointplot gives us histograms on each axis, which provides some
# interesting insights. The most common gear configuration seems to be 8, with
# 6 closely behind. And MPG ratings seem to roughly follow a bell curve
# centered at around 22 or so.
sns.jointplot(x="# Gears", y="CombMPG", data=df)


# boxplot
# The box plot shows us that the range of MPG values we see on each gearbox
# type aren't as crazily distributed as it seemed at first glance; many of
# the extreme values are in fact outliers that are best discarded when
# analyzing the trends. This makes the real relationships easier to see;
# those continuously variable transmissions with a single gear are really
# quite good at fuel efficiency (higher MPG's are more efficient). Between
# 5 and 8 things are roughly the same, but from 8-10 things decline markedly.
sns.boxplot(x="# Gears", y="CombMPG", data=df)


# swarmplot
# The swarm plot makes it even more apparent that those high MPG outliers are
# in fact outliers on the 6-gear vehicles; the vast majority of 6-gear
# vehcles have less than 32 MPG. And the overall trend is perhaps easiest
# to visualize and understand in this representation.
sns.swarmplot(
    data=df,
    x="# Gears",
    y="CombMPG",
    hue="# Gears",
    palette="deep",
)
plt.show()


# So, our final verdict: more gears result in worse fuel efficiency.
# This is surprising as a little counter-intuitive! But, this is real data from
# the US Department of Energy for 2019 model year cars, and that's a real
# conclusion we've drawn, thanks to Seaborn!
