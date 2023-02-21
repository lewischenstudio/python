"""
- Understand algorithms and data structures is very important for programmers
- Big O notations: O(1), O(N), O(N^2), O(log(N)), O(N*log(N))

Lists: slow
    - list.pop()            O(1)
    - list.pop(0)           O(N)
    - list.append(1)        O(1)
    - list.insert(0, 1)     O(N)

deques: double-ended queue / doubly-linked lists
    - collections.dequeue class
    - dequeue.pop()         O(1)
    - dequeue.popleft()     O(1)
    - dequeue.append(1)     O(1)
    - dequeue.appendleft(1) O(1)
    - dequeue[0]            O(1)
    - dequeue[N - 1]        O(1)
    - dequeue[int(N / 2)]   O(N) -- no good

bisect: binary search on sorted arrays
    - collection = [1, 2, 4, 5, 6]
    - bisect.bisect(collection, 3) -- O(log(N)) fast

Dictionaries are implemented as hash maps, each of which is data structure that associates a set of key-value pairs.
    - hash("hello")
    - access, insertion and removal of an item scales as O(1)
    - a set of key-value pairs
    - collections.defaultdict
    - Counter is the fastest

In-memory search
    - The inverted index is a structure that associates each word in our collection with the list of documents where
      that word is present.
    - Time complexity is O(1) with the drawback that one needs to encode every possible query
"""

import bisect
from collections import defaultdict, Counter


items = (i for i in range(1000))


def index_bisect(a, x):
    """Locate the leftmost value exactly equal to x"""
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def counter_dict(items):
    """Count the number of occurrences of each value in the list"""
    counter = {}
    for item in items:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
        return counter


def counter_defaultdict(items):
    """Using defaultdict to count occurrences"""
    counter = defaultdict(int)
    for item in items:
        counter[item] += 1
    return counter


counter = Counter(items)


docs = ["the cat is under the table", "the dog is under the table", "cats and dogs smell roses", "Carla eats an apple"]


def inverted_index(word: str, docs: list):
    """Inverted index technique to reduce the time complexity to O(1)"""
    # Building an index
    index = {}
    for i, doc in enumerate(docs):
        # We iterate over each term in the document
        for word in doc.split():
            # We build a list containing the indices where the term appears
            if word not in index:
                index[word] = [i]
            else:
                index[word].append(i)

    results = index[word]
    return [docs[i] for i in results]
