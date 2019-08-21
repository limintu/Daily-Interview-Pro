import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().staircase(4), 5)

    def test2(self):
        self.assertEqual(Solution().staircase(5), 8)


if __name__ == '__main__':
    unittest.main()
