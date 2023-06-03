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

Given a sequence, find the length of the longest palindromic subsequence 
in it using dynamic programming.

Palindrome is a string that reads the same backward as well as forward.

**Example:**

lps("ABABCBA") # 5


### Subset Sum Problem

Given a set of non-negative integers, and a value sum, determine if there 
is a subset of the given set with sum equal to given sum.

**Example**:

Input: [3, 34, 4, 12, 5, 2], sum = 9

Output: True  

There is a subset (4, 5) with sum 9.
 
Input: [3, 34, 4, 12, 5, 2], sum = 30

Output: False

There is no subset that add up to 30.


### Egg Dropping Puzzle

The following is a description of the instance of this famous puzzle 
involving N=2 eggs and a building with H=36 floors:

Suppose that we wish to know which stories in a 36-story building are 
safe to drop eggs from, and which will cause the eggs to break on landing. 
We make a few assumptions:
- An egg that survives a fall can be used again.
- A broken egg must be discarded.
- The effect of a fall is the same for all eggs.
- If an egg breaks when dropped, then it would break if dropped from a 
higher window.
- If an egg survives a fall, then it would survive a shorter fall.
- It is not ruled out that the first-floor windows break eggs, nor is it 
ruled out that eggs can survive the 36th-floor windows.

If only one egg is available and we wish to be sure of obtaining the right 
result, the experiment can be carried out in only one way. Drop the egg 
from the first-floor window; if it survives, drop it from the second-floor
window. Continue upward until it breaks. In the worst case, this method may
require 36 droppings. Suppose 2 eggs are available. What is the lowest number
of egg-droppings that is guaranteed to work in all cases?


### Maximum Length Chain of Pairs

You are given n pairs of numbers. In every pair, the first number is always
smaller than the second number. A pair (c, d) can follow another pair (a, b)
if b < c. Chain of pairs can be formed in this fashion. Find the longest
chain which can be formed from a given set of pairs.

Example

If the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} },
then the longest chain that can be formed is of length 3, and the chain is
{{5, 24}, {27, 40}, {50, 90}}