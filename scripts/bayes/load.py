import os
import io
import pickle
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB
import time
from scipy.sparse import csr_matrix, save_npz, load_npz

t1 = time.time()

file_urls = []


def readFiles(path):
    for root, _, filenames in os.walk(path):
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
    for file_url, message in readFiles(path):
        rows.append({"message": message, "class": classification})
        index.append(file_url)

    return DataFrame(rows, index=index)


data = DataFrame({"message": [], "class": []})

data = pd.concat([data, dataFrameFromDirectory("scripts/emails/spam", "spam")])
data = pd.concat([data, dataFrameFromDirectory("scripts/emails/ham", "ham")])

# data.head()

# Now we will use a CountVectorizer to split up each message into its list of words, and throw that into a MultinomialNB classifier.
# Call fit() and we've got a trained spam filter ready to go! It's just that easy.
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data["message"].values)

with open("count_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# with open("tfidf_vectorizer.pkl", "wb") as f:
#     pickle.dump(vectorizer, f)

# save_npz("my_sparse_matrix.npz", counts)
# print("Sparse matrix saved successfully!")

counts_matrix = load_npz("my_counts_matrix.npz")
# print("Sparse matrix loaded successfully!")
# print(counts_matrix)

# print("counts: ", counts)
# print(type(counts))
# dense_counts = counts.toarray()
# print("dense_counts: ", dense_counts)
# print("len: ", len(dense_counts))

# inverse_counts = vectorizer.inverse_transform(dense_counts)
# counts_2 = vectorizer.inverse_transform(inverse_counts)

# print("inverse_counts: ", inverse_counts)
# print("counts_2: ", counts_2)
# print(data["message"].values)
# print(type(data["message"].values))
# print(counts)
# print("counts: ", type(counts))

classifier = MultinomialNB()
# targets = data["class"].values
# print("targets: ", targets)

# w_file = open("my_targets_values", "w")
# for item in targets:
#     w_file.write(item + "\n")
# w_file.close()

r_file = open("my_targets_values", "r")
target_values = r_file.readlines()
r_file.close()
target_values = [line.replace("\n", "") for line in target_values]

# print("target_values: ", target_values)

# print("targets: ", len(targets))
classifier.fit(counts_matrix, target_values)

# vectorizer = CountVectorizer()
# vectorizer.inverse_transform(counts_matrix)
with open("count_vectorizer.pkl", "rb") as f:
    loaded_vectorizer = pickle.load(f)


examples = ["Free Viagra now!!!"]
example_counts = loaded_vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)

t2 = time.time()
elapsed_time_perf = t2 - t1
print(f"Elapsed time (perf_counter): {elapsed_time_perf:.6f} seconds")

# 271.434020 seconds
