"""Naive Bayes"""

import os
import io
from dotenv import load_dotenv
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

load_dotenv(os.path.join(os.getcwd(), ".env"))


def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, "r", encoding="latin1")
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == "\n":
                    inBody = True
            f.close()
            message = "\n".join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({"message": message, "class": classification})
        index.append(filename)

    return DataFrame(rows, index=index)


# For creating a database which has two columns
# "message" has the actual text of the email
# "class" specifies whether it is a spam or not
data = DataFrame({"message": [], "class": []})

data = data.append(dataFrameFromDirectory(os.environ.get("SPAM"), "spam"))
data = data.append(dataFrameFromDirectory(os.environ.get("HAM"), "ham"))

data.head()

# Now we will use a CountVectorizer to split up each message into its list of
# words, and throw that into a MultinomialNB classifier. Call fit() and we've
# got a trained spam filter ready to go! It's just that easy.
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data["message"].values)

classifier = MultinomialNB()
targets = data["class"].values
classifier.fit(counts, targets)

# Try it out
examples = ["Free Viagra now!!!", "Hi Bob, how about a game of golf tomorrow?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print("predictions: ", predictions)

examples = [
    "Your email greeting is one of the first things a reader sees, along with "
    + "your email name and the subject line. The greeting acts as the first "
    + "impression for both the contents of the email and you. ",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi"
    + "aliquip ex ea commodo consequat. ",
]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print("predictions: ", predictions)
