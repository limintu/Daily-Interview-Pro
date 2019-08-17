import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().check([13, 4, 7]), True)

    def test2(self):
        self.assertEqual(Solution().check([5, 1, 3, 2, 5]), False)

    def test3(self):
        self.assertEqual(Solution().check([5, 4, 7, 8]), True)

    def test4(self):
        self.assertEqual(Solution().check([5, 4, 7, 6]), False)

    def test5(self):
        self.assertEqual(Solution().check([4, 5, 3]), True)


if __name__ == '__main__':
    unittest.main()
