"""Count Primes"""

import math


class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if isPrime[i]:
                for multiples_of_i in range(i * 2, n, i):
                    isPrime[multiples_of_i] = False

        primeCount = 0
        for i in range(n):
            if isPrime[i]:
                primeCount += 1

        return primeCount


if __name__ == "__main__":
    print(Solution().countPrimes(1))
    print(Solution().countPrimes(5))
    print(Solution().countPrimes(10))
    print(Solution().countPrimes(17))
