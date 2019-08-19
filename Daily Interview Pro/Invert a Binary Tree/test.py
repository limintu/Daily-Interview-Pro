import unittest
from solution import Solution, TreeNode


class MyTestCase(unittest.TestCase):
    def test1(self):
        root = TreeNode('a')
        root.left = TreeNode('b')
        root.right = TreeNode('c')
        root.left.left = TreeNode('d')
        root.left.right = TreeNode('e')
        root.right.left = TreeNode('f')

        Solution().invert(root)
        result = []
        self.preorder_list(root, result)

        self.assertEqual(result, ['a', 'c', 'f', 'b', 'e', 'd'])

    def test2(self):
        root = TreeNode('a')
        root.left = TreeNode('b')
        root.right = TreeNode('c')
        root.left.left = TreeNode('d')

        Solution().invert(root)
        result = []
        self.preorder_list(root, result)

        self.assertEqual(result, ['a', 'c', 'b', 'd'])

    def preorder_list(self, root: TreeNode, tree: list) -> list:
        if root is None:
            return
        tree.append(root.val)
        self.preorder_list(root.left, tree)
        self.preorder_list(root.right, tree)


if __name__ == '__main__':
    unittest.main()
