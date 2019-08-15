import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
        x = 2
        self.assertEqual(Solution().searchRange(arr, x), [1, 4])

    def test2(self):
        arr = [5,7,7,8,8,10]
        x = 6
        self.assertEqual(Solution().searchRange(arr, x), [-1, -1])

    def test3(self):
        arr = [5,7,7,8,8,10]
        x = 8
        self.assertEqual(Solution().searchRange(arr, x), [3, 4])

    def test4(self):
        arr = []
        x = 0
        self.assertEqual(Solution().searchRange(arr, x), [-1, -1])
if __name__ == '__main__':
    unittest.main()
