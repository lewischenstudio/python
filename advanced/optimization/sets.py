"""
Sets are unordered collections of elements that must be unique.
    - addition, deletion and test for membership time complexities are O(1)
    - removing duplicates is O(N)
    - s.union(t)        O(S+T)
    - s.inersection(t)  O(min(S,T))
    - s.difference(t)   O(S)
    - application of intersection can use inverted index technique
"""

docs = ["the cat is under the table", "the dog is under the table", "cats and dogs smell roses", "Carla eats an apple"]

# create a list that contains duplicates
x = list(range(1000)) + list(range(500))
# the set *x_unique* will contain only the unique elements in x
x_unique = set(x)


# Building an index using sets
index = {}
for i, doc in enumerate(docs):
    # We iterate over each term in the document
    for word in doc.split():
        # We build a set containing the indices where the term appears
        if word not in index:
            index[word] = {i}
        else:
            index[word].add(i)
# Querying the documents containing both "cat" and "table"
index["cat"].intersection(index["table"])
