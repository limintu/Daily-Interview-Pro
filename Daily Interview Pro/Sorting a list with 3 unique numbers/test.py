import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        test = [3, 3, 2, 1, 3, 2, 1]
        ans = [1, 1, 2, 2, 3, 3, 3]
        self.assertEqual(Solution().sortNums(test), ans)

    def test2(self):
        test = [3, 2, 1, 1, 1, 2, 3]
        ans = [1, 1, 1, 2, 2, 3, 3]
        self.assertEqual(Solution().sortNums(test), ans)

    def test3(self):
        test = [3, 3, 3, 1, 1, 1, 2]
        ans = [1, 1, 1, 2, 3, 3, 3]
        self.assertEqual(Solution().sortNums(test), ans)

    def test4(self):
        test = [3, 3, 3, 1, 1, 1, 1]
        ans = [1, 1, 1, 1, 3, 3, 3]
        self.assertEqual(Solution().sortNums(test), ans)


if __name__ == '__main__':
    unittest.main()
