import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().isValid("()(){(())"), False)

    def test2(self):
        self.assertEqual(Solution().isValid(""), True)

    def test3(self):
        self.assertEqual(Solution().isValid("([{}])()"), True)


if __name__ == '__main__':
    unittest.main()


