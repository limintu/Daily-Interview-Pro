import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def test1(self):
        graph = [['F', 'A', 'C', 'I'],
                 ['O', 'B', 'Q', 'P'],
                 ['A', 'N', 'O', 'B'],
                 ['M', 'A', 'S', 'S']]
        self.assertEqual(Solution().word_search(graph, "FOAM"), True)

    def test2(self):
        graph = [['F', 'A', 'C', 'I'],
                 ['O', 'B', 'Q', 'P'],
                 ['A', 'N', 'O', 'B'],
                 ['M', 'A', 'S', 'S']]
        self.assertEqual(Solution().word_search(graph, "ABQOB"), True)

    def test3(self):
        graph = [['F', 'A', 'C', 'I'],
                 ['O', 'B', 'Q', 'P'],
                 ['A', 'N', 'O', 'B'],
                 ['M', 'A', 'S', 'S']]
        self.assertEqual(Solution().word_search(graph, "ABCD"), False)


if __name__ == '__main__':
    unittest.main()
