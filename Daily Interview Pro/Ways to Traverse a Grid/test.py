import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().num_ways(2, 2), 2)

    def test2(self):
        self.assertEqual(Solution().num_ways(3, 3), 6)

    def test3(self):
        self.assertEqual(Solution().num_ways(7, 3), 28)

    def test4(self):
        self.assertEqual(Solution().num_ways(1, 3), 1)


if __name__ == '__main__':
    unittest.main()
