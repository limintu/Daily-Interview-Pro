import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def test1(self):
        graph = [['F', 'A', 'C', 'I'],
                 ['O', 'B', 'Q', 'P'],
                 ['A', 'N', 'O', 'B'],
                 ['M', 'A', 'S', 'S']]
        self.assertEqual(Solution().word_search(graph, "FOAM"), False)


if __name__ == '__main__':
    unittest.main()
