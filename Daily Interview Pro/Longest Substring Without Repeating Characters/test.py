import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"), 10)

    def test2(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('abcabcbb'), 3)

    def test3(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('bbbbb'), 1)

    def test4(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('pwwkew'), 3)


if __name__ == '__main__':
    unittest.main()
