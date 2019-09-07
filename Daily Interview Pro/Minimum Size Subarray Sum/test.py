import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().minSubArrayLen(3, [1, 1]), 0)

    def test2(self):
        self.assertEqual(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test3(self):
        self.assertEqual(Solution().minSubArrayLen(4, [0, 4, 4]), 1)


if __name__ == '__main__':
    unittest.main()
