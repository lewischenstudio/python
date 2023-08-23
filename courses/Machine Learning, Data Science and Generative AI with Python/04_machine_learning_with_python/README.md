## Section 04: Machine Learning with Python

#### Table of Contents
- Supervised vs. Unsupervised Learning, and Train/Test
- Using Train/Test to Prevent Overfitting a Polynomial Regression
- Bayesian Methods: Concepts
- Implementing a Spam Classifier with Naive Bayes
- K-Means Clustering
- Clustering people based on income and age
- Measuring Entropy
- WINDOWS: Installing Graphviz
- MAC: Installing Graphviz
- LINUX: Installing Graphviz
- Decision Trees: Concepts
- Decision Trees: Predicting Hiring Decisions
- Ensemble Learning
- XGBoost
- Support Vector Machines (SVM) Overview


### Supervised vs. Unsupervised Learning, and Train/Test

#### What is machine learning?
- Algorithms that can learn from observational data and can make predictions based on it

#### Unsupervised Learning
- The model is not given any "answers" to learn from
- It must make sense of the data just given the observations themselves
- Example: group (cluster) some objects together into 2 different sets. But I don't tell 
  you want tht "right" set is for any object ahead of time.
  - Do I want big and small things? Round and square things? Red and blue things?
  - Unsupervised learning could give me any of those results

#### Unsupervised Learning
- Unsupervised learning sounds awful! Why use it?
- Maybe you don't know waht you're looking for -- you're looking for _latent variables_.
- Example: clustering users on a dating site based on their information and behavior. Perhaps
  you'll find there are groups of people that emerge that don't conform to your known stereotypes.
- Cluster movies based on their properties. Perhaps our current concepts of genre are outdated?
- Analyze the text of product descriptions to find the terms that carry the most meaning for a 
  certain category.


#### Supervised Learning
- In supervised learning, the data the algorithm "learns" from comes with the "correct" answers.
- The model created is then used to predict the answer for new, unknown values.
- Example: You can _train_ a model for predicting car prices based on car attributes using 
  historical sales data. That model can then predict the optimal price for new cars that 
  haven't been sold before.

#### Evaluating Supervised Learning
- If you have a set of training data that includes the value you're trying to predict -- you don't
  have to guess if the resulting model is good or not.
- If you have enough training data, you can split it into two parts: a _training_ set and a _test_
  set.
- You then train the model using only the training set
- And then measure (using r-squared or some other metric) the model's accuracy by asking it to 
  predict values for the test set, and compare that to the known, true values.


#### Train / Test in practice
- Need to ensure both sets are large enough to contain representatives of all the variations and
  outliers in the data you care about
- The data sets must be selected randomly
- Train/test is a great way to guard against _overfitting_

#### Train/Test is not Infallible
- Maybe your sample sizes are too small
- Or due to random chance your train and test sets look remarkably similar
- Overfitting can still happen

![Infallible](https://github.com/lcycstudio/python/blob/master/courses/Machine%20Learning%2C%20Data%20Science%20and%20Generative%20AI%20with%20Python/04_machine_learning_with_python/infallible.png)


#### K-fold Cross Validation
- One way to further protect against overfitting is K-fold cross validation 
- Sounds complicated. But it’s a simple idea: 
  - Split your data into K randomly-assigned segments
  - Reserve one segment as your test data
  - Train on each of the remaining K-1 segments and measure their performance against the 
    test set
  - Take the average of the K-1 r-squared scores



### Using Train/Test to Prevent Overfitting a Polynomial Regression

Refer to `train_test.py` for coding exercises.


### Bayesian Methods: Concepts

#### Remember Bayes' Theorem
- $P(A|B) = \frac{P(A)P(B|A)}{P(B)}$
- Let's use it for machine learning! I want a spam classifier.
- Example: how would we express the probability of an email being spam if it 
  contains the word "free"?
- $P(Spam|Free) = \frac{P(Spam)P(Free|Spam)}{P(Free)}$
- The numerator is the probability of a message being spam and containing the word
  "free" (this is subtly different from what we're looking for)
- The denominator is the overall probability of an email containing the word "free".
  This is equivalent to $P(Free|Spam)P(Spam) + P(Free|Not Spam)P(Not Spam)$.
- So together, this ratio is the percentage of emails with the word "free" that are spam.

#### What about all other words?
- We can construct $P(Spam | Word)$ for every meaningful word we encounter during training
- Then multiply these together when analyzing a new email to get the probability of it 
  is being spam.
- Assumes the presence of different words are independent of each other -- one reason this
  is called "Naive Bayes".

#### Sounds like a lot of work
- Scikit-learn to the rescue!
- The CountVectorizer lets us operate on lots of words at once, and MultinominalNB does all
  the heavy lifting on Naive Bayes.
- We'll train it on known sets of spam and "ham" (non-spam) emails
  - So this is supervised learning



### Implementing a Spam Classifier with Naive Bayes

Refer to `naive_bayes.py` for coding exercises.



### K-Means Clustering



### Clustering people based on income and age



### Measuring Entropy



### WINDOWS: Installing Graphviz



### MAC: Installing Graphviz



### LINUX: Installing Graphviz



### Decision Trees: Concepts



### Decision Trees: Predicting Hiring Decisions



### Ensemble Learning



### XGBoost



### Support Vector Machines (SVM) Overview





