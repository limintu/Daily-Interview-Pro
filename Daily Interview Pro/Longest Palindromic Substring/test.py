import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().longestPalindrome("banana"), "anana")

    def test2(self):
        self.assertEqual(Solution().longestPalindrome("million"), "illi")


if __name__ == '__main__':
    unittest.main()
