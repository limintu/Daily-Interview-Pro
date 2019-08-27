import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().calculate('1 + 1'), 2)

    def test2(self):
        self.assertEqual(Solution().calculate(' 2-1 + 2 '), 3)

    def test3(self):
        self.assertEqual(Solution().calculate('(1+(4+5+2)-3)+(6+8)'), 23)

    def test4(self):
        self.assertEqual(Solution().calculate('- (3 + ( 2 - 1 ) )'), -4)


if __name__ == '__main__':
    unittest.main()
