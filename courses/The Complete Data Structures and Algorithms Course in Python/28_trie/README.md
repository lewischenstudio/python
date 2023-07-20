## Section 26: Binary Heap

#### Table of Contents
- What is a Trie? Why we need it?
- Common Operations on Trie (Creation)
- Insert a string in Trie
- Search for a string in Trie
- Delete a string from Trie
- Practical use of Trie

### What is a Trie? Why we need it?

A Trie is a tree-based data structure that organizes information in a hierarchy.

**Properties**
- It is typically used to store or search things in a space and time efficient way.
- Any node in trie can store non repetitive multiple characters
- Every node stores link of the next character of the string
- Every node keeps track of "end of string"
```
                AB
              /    \  
             /      \  
           /          \  
          I           AIM
        /           /  |  \ 
       /           /   |   \ 
     RT           R    L    . 
    /  \         /
   .    .       .
```

#### Why we need Trie?
To solve many standard problems in efficient way
- Spelling checker
- Auto completion


### Common Operations on Trie
- Creation of Trie
- Insertion of Trie
- Search for string in Trie
- Deletion from Trie
- Practical use of Trie