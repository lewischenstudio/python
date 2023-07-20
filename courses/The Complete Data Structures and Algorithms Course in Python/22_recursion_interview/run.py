"""
A recursion class that consists of all the functions listed in this section
"""
import unittest


class Recursion:
    def __init__(self) -> None:
        self.error = "The number must be postive integer only!"

    def decimalToBinary(self, a):
        assert a >= 0 and int(a) == a, self.error
        if a == 0:
            return 0
        return a % 2 + 10 * self.decimalToBinary(int(a / 2))

    def gcd(self, a, b):
        """
        The Greatest Common Divisor of two numbers using recursion
        """
        assert int(a) == a and int(b) == b, self.error
        if a < 0:
            a = -1 * a
        if b < 0:
            b = -1 * b
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def powerOfNumber(self, x, n):
        """
        The power of a number using recursion
        """
        assert n >= 0 and int(n) == n, self.error
        if n in [0, 1]:
            return x
        return x * self.powerOfNumber(x, n - 1)

    def sumOfDigits(self, n):
        """
        The sum of digits of a positive integer number using recursion
        """
        assert n >= 0 and int(n) == n, "The number must be postive integer only!"
        if n in [0, 1]:
            return int(n)
        return int(n % 10) + self.sumOfDigits(int(n / 10))


class TestRecursion(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.class_ = Recursion()
        super().__init__(methodName)

    def test_decimalToBinary(self) -> None:
        self.assertEqual(self.class_.decimalToBinary(3), 11)
        with self.assertRaises(AssertionError):
            self.class_.decimalToBinary(-3)

    def test_gcd(self) -> None:
        self.assertEqual(self.class_.gcd(36, 48), 12)
        self.assertEqual(self.class_.gcd(-36, 48), 12)

    def test_powerOfNumber(self) -> None:
        self.assertEqual(self.class_.powerOfNumber(3, 3), 27)
        self.assertEqual(self.class_.powerOfNumber(-3, 3), -27)

    def test_sumOfDigits(self) -> None:
        self.assertEqual(self.class_.sumOfDigits(312), 6)
        with self.assertRaises(AssertionError):
            self.class_.sumOfDigits(-3)


if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
