"""
Tries are extremely fast at matching a list of strings agains a prefix.
    - pip install patricia-trie
    - O(S)
    - Algorithm     N=10000(mus)    N=20000(mus)    N=30000(mus)    Time
    - Trie          17.12           17.27           17.47           O(S)
    - Linear Scan   1978.44         4075.72         6398.06         O(SN
"""
import time
from random import choice
from string import ascii_uppercase
from patricia import trie


# Patricia strings
# 1. List implementation
def random_string(length):
    """Produce a random string made of *length* uppercase ascii characters"""
    return "".join(choice(ascii_uppercase) for i in range(length))


strings = [random_string(32) for i in range(10000)]
matches = [s for s in strings if s.startswith("AA")]
t0 = time.time()
[s for s in strings if s.startswith("AA")]
t1 = time.time()
elapsed = t1 - t0

# 2. Patricia Tries
strings_dict = {s: 0 for s in strings}
# A dictionary where all values are 0
strings_trie = trie(**strings_dict)
# query patricia-trie for a matching prefix
t0 = time.time()
matches = list(strings_trie.iter("AA"))
t1 = time.time()
elapsed = t1 - t0
