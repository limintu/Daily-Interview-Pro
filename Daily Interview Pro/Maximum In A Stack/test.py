import unittest
from solution import MaxStack


class MyTestCase(unittest.TestCase):
    def test1(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertEqual(s.max(), 3)
        # 3
        s.pop()
        s.pop()
        self.assertEqual(s.max(), 2)
        # 2

    def test2(self):
        s = MaxStack()
        s.push(5)
        s.push(1)
        s.push(5)
        self.assertEqual(s.max(), 5)
        s.pop()
        self.assertEqual(s.max(), 5)
        s.pop()
        self.assertEqual(s.max(), 5)
        s.pop()
        self.assertEqual(s.max(), None)


if __name__ == '__main__':
    unittest.main()
