import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().distance('biting', 'sitting'), 2)

    def test2(self):
        self.assertEqual(Solution().distance('horse', 'ros'), 3)

    def test3(self):
        self.assertEqual(Solution().distance('intention', 'execution'), 5)


if __name__ == '__main__':
    unittest.main()
