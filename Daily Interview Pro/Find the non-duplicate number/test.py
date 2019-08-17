import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]), 1)

    def test2(self):
        self.assertEqual(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2, 1, 8]), 8)


if __name__ == '__main__':
    unittest.main()

