"""Count Primes"""


class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        count = 0
        for i in range(2, n):
            isPrime = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                count += 1

        return count


if __name__ == "__main__":
    print(Solution().countPrimes(1))
    print(Solution().countPrimes(5))
    print(Solution().countPrimes(10))
    print(Solution().countPrimes(17))
