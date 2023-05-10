"""
A recursion class that consists of all the functions listed in this section
"""
import unittest


class RecursionExercises:
    def __init__(self) -> None:
        self.number_error = "Input value must be float or integer"
        self.integer_error = "Input must be postive integer only!"
        self.string_error = "Input value must be string!"
        self.array_error = "Input value must be a non-empty array!"
        self.object_error = "Input must be an object!"

    def passConstraint(self, val):
        return isinstance(val, float) or isinstance(val, int)

    def power(self, base, exponent):
        assert self.passConstraint(base), self.number_error
        assert self.passConstraint(exponent), self.number_error
        if exponent <= 0:
            return base**exponent
        return base * self.power(base, exponent - 1)

    def factorial(self, num):
        assert num >= 0 and int(num) == num, self.integer_error
        if num in (0, 1):
            return 1
        return num * self.factorial(num - 1)

    def productOfArray(self, arr) -> float:
        for i in arr:
            assert float(i) == i or int(i) == i, self.number_error
        if len(arr) <= 1:
            return arr[0]
        return arr[0] * self.productOfArray(arr[1 : len(arr)])

    def recursiveRange(self, num):
        assert float(num) == num or int(num) == 0, self.number_error
        if num <= 0:
            return num
        return num + self.recursiveRange(num - 1)

    def fib(self, num):
        assert num >= 0 and int(num) == num, self.integer_error
        if num in [0, 1]:
            return num
        return self.fib(num - 1) + self.fib(num - 2)

    def reverse(self, strng):
        assert isinstance(strng, str), self.string_error
        str_to_list = list(strng)
        if len(str_to_list) == 1:
            return str_to_list[0]
        return str_to_list[-1] + self.reverse("".join(str_to_list[0:-1]))

    def isPalindrome(self, strng):
        assert str(strng) == strng, self.string_error
        str_to_list = list(strng)
        if len(str_to_list) == 1:
            return True
        if len(str_to_list) == 2:
            return str_to_list[0] == str_to_list[1]
        if str_to_list[0] == str_to_list[-1]:
            return self.isPalindrome("".join(str_to_list[1 : len(str_to_list) - 1]))
        return False

    def isOdd(self, num):
        if num % 2 == 0:
            return False
        else:
            return True

    def someRecursive(self, arr):
        assert isinstance(arr, list) and len(arr) > 0, self.array_error
        if len(arr) == 1:
            return self.isOdd(arr[0])
        if self.isOdd(arr[0]):
            return self.isOdd(arr[0])
        return self.someRecursive(arr[1:])

    def flatten(self, arr):
        assert isinstance(arr, list), "Input must be an array!"
        if len(arr) == 0:
            return arr
        if isinstance(arr[0], list):
            if len(arr[0]) > 1:
                return self.flatten([arr[0][0]] + [arr[0][1:]] + arr[1:])
            return self.flatten([arr[0][0]] + arr[1:])
        return [arr[0]] + self.flatten(arr[1:])

    def checkString(self, arr):
        for item in arr:
            if not isinstance(item, str):
                return False
        return True

    def capitalizeFirst(self, arr):
        assert type(arr) is list, self.array_error
        assert self.checkString(arr), self.string_error
        if len(arr) == 0:
            return []
        return [arr[0][0].upper() + arr[0][1:]] + self.capitalizeFirst(arr[1:])

    def nestedEvenSum(self, obj, sum=0):
        assert type(obj) is dict, self.object_error
        new_sum = sum
        for value in obj.values():
            if type(value) is dict:
                new_sum = self.nestedEvenSum(value, new_sum)
            elif type(value) is float or type(value) is int:
                if value % 2 == 0:
                    new_sum = new_sum + value
        return new_sum

    def capitalizeWords(self, arr):
        assert type(arr) is list, self.array_error
        assert self.checkString(arr), "Each item in the array must be string!"
        if len(arr) == 0:
            return []
        return [arr[0].upper()] + self.capitalizeWords(arr[1:])

    def stringifyNumbers(self, obj):
        assert type(obj) is dict, self.object_error
        new_obj = {}
        for key, value in obj.items():
            if type(value) is dict:
                new_obj[key] = self.stringifyNumbers(value)
            elif type(value) is float or type(value) is int:
                new_obj[key] = str(value)
            else:
                new_obj[key] = value
        return new_obj

    def collectStrings(self, obj):
        assert type(obj) is dict, self.object_error
        arr = []
        for value in obj.values():
            if type(value) is str:
                arr.append(value)
            elif type(value) is dict:
                arr.extend(self.collectStrings(value))
        return arr


class TestRecursionExercises(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.class_ = RecursionExercises()
        super().__init__(methodName)

    def test_power(self) -> None:
        self.assertEqual(self.class_.power(3, 3), 27)
        with self.assertRaises(AssertionError):
            self.class_.power("-3", "3")

    def test_factorial(self) -> None:
        self.assertEqual(self.class_.factorial(4), 24)
        with self.assertRaises(AssertionError):
            self.class_.factorial(-3)
            self.class_.factorial(3.4)

    def test_productOfArray(self) -> None:
        self.assertEqual(self.class_.productOfArray([1, 2, 3]), 6)
        self.assertEqual(self.class_.productOfArray([4, 5, 6]), 120)
        with self.assertRaises(AssertionError):
            self.class_.productOfArray(["3"])

    def test_recursiveRange(self) -> None:
        self.assertEqual(self.class_.recursiveRange(6), 21)
        self.assertEqual(self.class_.recursiveRange(9), 45)
        with self.assertRaises(AssertionError):
            self.class_.recursiveRange("3")

    def test_fib(self) -> None:
        self.assertEqual(self.class_.fib(6), 8)
        self.assertEqual(self.class_.fib(9), 34)
        with self.assertRaises(AssertionError):
            self.class_.fib(-3)
            self.class_.fib(3.5)

    def test_reverse(self) -> None:
        self.assertEqual(self.class_.reverse("python"), "nohtyp")
        self.assertEqual(self.class_.reverse("reverse"), "esrever")
        with self.assertRaises(AssertionError):
            self.class_.reverse(3)

    def test_isPalindrome(self) -> None:
        self.assertFalse(self.class_.isPalindrome("awesome"))
        self.assertFalse(self.class_.isPalindrome("foobar"))
        self.assertFalse(self.class_.isPalindrome("amanaplanacanalpandemonium"))
        self.assertTrue(self.class_.isPalindrome("tacocat"))
        self.assertTrue(self.class_.isPalindrome("amanaplanacanalpanama"))
        self.assertTrue(self.class_.isPalindrome("1001001"))
        with self.assertRaises(AssertionError):
            self.class_.isPalindrome(3)

    def test_someRecursive(self) -> None:
        self.assertTrue(self.class_.someRecursive([1, 2, 3, 4]))
        self.assertTrue(self.class_.someRecursive([4, 6, 8, 9]))
        self.assertFalse(self.class_.someRecursive([4, 6, 8]))
        with self.assertRaises(AssertionError):
            self.class_.someRecursive(3)

    def test_flatten(self) -> None:
        self.assertEqual(self.class_.flatten([1, 2, 3, [4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(self.class_.flatten([1, [2, [3, 4], [[5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(self.class_.flatten([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(self.class_.flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]), [1, 2, 3])
        with self.assertRaises(AssertionError):
            self.class_.flatten(-3)
            self.class_.flatten(3.5)

    def test_capitalizeFirst(self) -> None:
        self.assertEqual(self.class_.capitalizeFirst(["car", "taco", "banana"]), ["Car", "Taco", "Banana"])
        with self.assertRaises(AssertionError):
            self.class_.capitalizeFirst(-3)
            self.class_.capitalizeFirst([3.5])

    obj1 = {"outer": 2, "obj": {"inner": 2, "otherObj": {"superInner": 2, "notANumber": True, "alsoNotANumber": "yup"}}}

    obj2 = {
        "a": 2,
        "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
        "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
        "d": 1,
        "e": {"e": {"e": 2}, "ee": "car"},
    }

    def test_nestedEvenSum(self) -> None:
        self.assertEqual(self.class_.nestedEvenSum(self.obj1), 6)
        self.assertEqual(self.class_.nestedEvenSum(self.obj2), 10)
        with self.assertRaises(AssertionError):
            self.class_.nestedEvenSum(-3)
            self.class_.nestedEvenSum([3.5])

    def test_capitalizeWords(self) -> None:
        self.assertEqual(
            self.class_.capitalizeWords(["i", "am", "learning", "recursion"]), ["I", "AM", "LEARNING", "RECURSION"]
        )
        with self.assertRaises(AssertionError):
            self.class_.capitalizeWords(-3)
            self.class_.capitalizeWords([3.5])

    obj3 = {"num": 1, "test": [], "data": {"val": 4, "info": {"isRight": True, "random": 66}}}
    obj4 = {"num": "1", "test": [], "data": {"val": "4", "info": {"isRight": True, "random": "66"}}}
    obj5 = {
        "stuff": "foo",
        "data": {"val": {"thing": {"info": "bar", "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}}}}},
    }

    def test_stringifyNumbers(self) -> None:
        self.assertEqual(self.class_.stringifyNumbers(self.obj3), self.obj4)
        with self.assertRaises(AssertionError):
            self.class_.stringifyNumbers(-3)
            self.class_.stringifyNumbers([3.5])

    def test_collectStrings(self) -> None:
        self.assertEqual(self.class_.collectStrings(self.obj5), ["foo", "bar", "baz"])
        with self.assertRaises(AssertionError):
            self.class_.collectStrings(-3)
            self.class_.collectStrings([3.5])


if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
