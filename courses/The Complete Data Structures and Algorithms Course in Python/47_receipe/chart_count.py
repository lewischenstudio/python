"""
Write a function which takes in a string and returns count of
each character in the string
"""
import unittest


def charCount(text: str) -> dict:
    if not isinstance(text, str):
        return "Input type must be string"
    my_dict = {}
    for i in text.lower():
        if not (i.isspace()):
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
    return my_dict


class Test(unittest.TestCase):
    def test_charCount(self):
        self.assertEqual(charCount("bbbb"), {"b": 4})
        self.assertEqual(charCount("hello"), {"h": 1, "e": 1, "l": 2, "o": 1})
        self.assertEqual(
            charCount("My name is Lewis"),
            {
                "m": 2,
                "y": 1,
                "n": 1,
                "a": 1,
                "e": 2,
                "i": 2,
                "s": 2,
                "l": 1,
                "w": 1,
            },
        )
        self.assertEqual(charCount(""), {})
        self.assertEqual(charCount(1), "Input type must be string")


if __name__ == "__main__":
    unittest.main()
