import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().two_sum([4, 7, 1, -3, 2], 5), True)

    def test2(self):
        self.assertEqual(Solution().two_sum([2, 7, 11, 15], 9), True)

    def test3(self):
        self.assertEqual(Solution().two_sum([2, 7, 11, 15], 12), False)

if __name__ == '__main__':
    unittest.main()
