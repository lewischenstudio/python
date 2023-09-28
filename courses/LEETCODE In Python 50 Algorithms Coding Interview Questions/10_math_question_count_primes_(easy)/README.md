## Section 10: Math Question: Count Primes (Easy)

#### Table of Contents

- Problem Introduction And Brute Force Explanation
- Pseudocode Walkthrough For Brute Force Approach
- Approach 2: Optimal solution
- Pseudocode Walkthrough For Optimal Approach
- Code Implementation

### Problem Introduction And Brute Force Explanation

Given an integer n, return the number of prime numbers that are strictly less than n.

[204. Count Primes](https://leetcode.com/problems/count-primes/)

### Pseudocode Walkthrough For Brute Force Approach

```
countPrimes(input) {
    if (input < 2) {
        return 0
    }
    count = 0
    for i in range[2: input] {
        isPrime = true
        for j in range[2: i] {
            if ( i % j == 0) {
                isPrime = false
                break
            }
        }
        if (isPrime == true) {
            count += 1
        }
    }
}
```

### Approach 2: Optimal solution

#### What defines a prime number?

- Bigger than 1
- Only divisile by itself and 1
  This means that if we find a prime number, we woukd **know** that all of its multiples are
  divisible by it, meaning that all multiples of prime numbers are not prime numbers.

Assume we consider ALL numbers up to N (the input) to be prime, our question now becomes
marking the non-prime numbers are non-prime.

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| 8   | 9   | 10  | 11  | 12  | 13  | 14  |
| 15  | 16  | 17  | 18  | 19  | 20  | 21  |
| 22  | 23  | 24  | 25  | 26  | 27  | 28  |
| 29  | 30  | 31  | 32  | 33  | 34  | 35  |

First element we look at is 2, we'll find that we consider 2 as prime, so next, we want to
set all of its multiples to false/non-prime.
2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34

Second element we look at is 3, we see that we consider 3 as a prime, so we want to set all
multiples of 3 to be false/non-prime.
3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33

Second element we look at is 5, we see that we consider 5 as a prime, so we want to set all
multiples of 5 to be false/non-prime.
5, 10, 15, 20, 25, 30, 35

We know that for every given prime number, i, we start setting its multiples to non-prime
starting from `i*i`, this means that if `i*i` exceeds our input, `n`, we should stop.

`6*6=36` is bigger than our `n` (which is 34), that means that there is no point in counting
any further.

```
countPrimes(n) {
    if (n <= 2) {
        return n
    }
    isPrime = [true] * n
    isPrime[0] = isPrime[1] = false
    for i in range[2 to sqrt(n)] {
        if (isPrime[i]) {
            for multiple_of_i in range[i*i to n, increment by 1] {
                isPrime[multiple_of_i] = false
            }
        }
    }
    return No.of "true" in isPrime
}
```

### Pseudocode Walkthrough For Optimal Approach

### Code Implementation
