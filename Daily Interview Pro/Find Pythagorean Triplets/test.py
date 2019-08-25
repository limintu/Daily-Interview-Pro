import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findPythagoreanTriplets([3, 5, 12, 5, 13]), True)

    def test2(self):
        self.assertEqual(Solution().findPythagoreanTriplets([3, 5, 12, 5, 4]), True)

    def test3(self):
        self.assertEqual(Solution().findPythagoreanTriplets([3, 5, 12, 5, 9]), False)


if __name__ == '__main__':
    unittest.main()
