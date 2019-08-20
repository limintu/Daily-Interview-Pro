import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [4, 3, 2, 4, 1, 3, 2]
        self.assertEqual(Solution().singleNumber(nums), 1)

    def test2(self):
        nums = [4, 3, 2, 4, 1, 3, 2, 1, 5]
        self.assertEqual(Solution().singleNumber(nums), 5)

    def test3(self):
        nums = [4, 3, 2, 1, 1, 3, 2]
        self.assertEqual(Solution().singleNumber(nums), 4)


if __name__ == '__main__':
    unittest.main()
