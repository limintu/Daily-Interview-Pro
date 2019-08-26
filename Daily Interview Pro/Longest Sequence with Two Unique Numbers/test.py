import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findSequence([1, 3, 5, 3, 1, 3, 1, 5]), 4)
        # [3, 1, 1, 3]

    def test2(self):
        self.assertEqual(Solution().findSequence([1, 3, 3, 3, 1, 1, 5, 3, 1, 3, 1, 5]), 6)
        # [1, 3, 3, 3, 1, 1]

    def test3(self):
        self.assertEqual(Solution().findSequence([1, 3, 5]), 2)
        # [1, 3] or [3, 5]


if __name__ == '__main__':
    unittest.main()
