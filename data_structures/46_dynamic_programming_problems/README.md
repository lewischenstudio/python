## Section 46: Dynamic Programming Problems

#### Table of Contents
- Longest repeated Subsequence Length Problem
- Longest Common Subsequence Length Problem
- Longest Common Subsequence Problem
- Diff Utility
- Shortest Common Supersequence Problem
- Length of Longest Palindromic Subsequence
- Subset Sum Problem
- Egg Dropping Puzzle
- Maximum Length Chain of Pairs

### Longest repeated Subsequence Length Problem
Create a function to find the length of Longest Repeated Subsequence. 
The longest repeated subsequence (LRS) is the longest subsequence of a
string that occurs at least twice.

**Example**
LRSLength('ATAKTKGGA', 9, 9) 
Answer: 4 ('ATKG')

Note: 9 is the length of the string.


### Longest Common Subsequence Length Problem

S1 and S2 are given strings, create a function to find the length of
the longest subsequence which is common to both strings.

Subsequence: a sequence that can be driven from another sequence by 
deleting some elements without changing the order of them

**Example**
S1 = "ABCBDAB"

S2 = "BDCABA"

LCSLength(S1, S2, len(S1), len(S2)) #4


### Longest Common Subsequence String Problem

S1 and S2 are given strings, create a function to print all possible 
longest subsequence which is common to both strings.

Subsequence: a sequence that can be driven from another sequence by 
deleting some elements without changing the order of them

**Example**

Input:
 
S1 = "ABCBDAB"

S2 = "BDCABA"
 
Ouput:
 
"BCAB"

"BCBA"

"BDAB"



### Diff Utility

Given two similar strings, implement your own diff utility to list
out all differences between them.

**Diff Utility**: It is a data comparison tool that calculates and
displays the differences between two text.

**Example**

Input:

S1 = 'XMJYAUZ'

S2 = 'XMJAATZ'

Output:

XMJ-YA-U+A+TZ

- indicates that character is deleted from S2 but it was present in S1

+ indicates that character is inserted in S2 but it was not present in S1

**Hint:**

You can use Longest Common Subsequence (LCS) to solve this problem. The
idea is to find a longest sequence of characters that is present in both
original sequences in the same order. From a longest common subsequence
it is only a small step to get diff-like output:
- if a character is absent in the subsequence but present in the first
original sequence, it must have been deleted (indicated by the '-' marks)
- if it is absent in the subsequence but present in the second original
sequence, it must have been inserted (indicated by the '+' marks)


### Shortest Common Supersequence Problem

The shortest common super sequence (SCS) is the problem of finding the
shortest super sequence supSeq of given sequences S1 and S2 such that
both these sequences are subseqeunce of supSeq.

**Example**

S1 = "ABCBDAB"

S2 = "BDCABA"
 
SCSLength(S1, S2, len(S1), len(S2)) #9



### Length of Longest Palindromic Subsequence


### Subset Sum Problem


### Egg Dropping Puzzle


### Maximum Length Chain of Pairs

