"""
A recursion class that consists of all the functions listed in this section
"""
import unittest


class Recursion:
    def __init__(self) -> None:
        self.error = "The number must be postive integer only!"

    def factorial(self, n):
        """
        The product of all positive integers less than or equal to 0
        """
        assert n >= 0 and int(n) == n, self.error
        if n in [0, 1]:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        """
        Fibonacci sequence is a sequence of numbers in which each number is the sum
        of the two preceding ones and the sequence starts from 0 and 1
        """
        assert n >= 0 and int(n) == n, self.error
        if n in [0, 1]:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


class TestRecursion(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.class_ = Recursion()
        super().__init__(methodName)

    def test_factorial(self) -> None:
        self.assertEqual(self.class_.factorial(4), 24)
        with self.assertRaises(AssertionError):
            self.class_.factorial(-3)

    def test_fibonacci(self) -> None:
        self.assertEqual(self.class_.fibonacci(4), 3)
        with self.assertRaises(AssertionError):
            self.class_.fibonacci(-3)


if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
