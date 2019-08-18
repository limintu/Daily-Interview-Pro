import unittest
from solution import Solution, TreeNode


class MyTestCase(unittest.TestCase):
    def test1(self):
        root = TreeNode(8)
        root.left = TreeNode(4)
        root.right = TreeNode(12)

        root.left.left = TreeNode(2)
        root.left.right = TreeNode(6)

        root.right.left = TreeNode(10)
        root.right.right = TreeNode(14)

        self.assertEqual(Solution().findCeilingFloor(root, 5), [4, 6])

    def test2(self):
        root = TreeNode(8)
        insertNode(root, 4)
        insertNode(root, 12)
        insertNode(root, 2)
        insertNode(root, 6)
        insertNode(root, 10)
        insertNode(root, 14)

        self.assertEqual(Solution().findCeilingFloor(root, 6), [6, 6])

    def test3(self):
        root = TreeNode(8)
        insertNode(root, 4)
        insertNode(root, 12)
        insertNode(root, 2)
        insertNode(root, 6)
        insertNode(root, 10)
        insertNode(root, 14)

        self.assertEqual(Solution().findCeilingFloor(root, 13), [12, 14])

    def test4(self):
        root = TreeNode(8)
        insertNode(root, 4)
        insertNode(root, 12)
        insertNode(root, 2)
        insertNode(root, 6)
        insertNode(root, 10)
        insertNode(root, 14)

        self.assertEqual(Solution().findCeilingFloor(root, 15), None)

    def test5(self):
        root = TreeNode(8)
        insertNode(root, 4)
        insertNode(root, 12)
        insertNode(root, 2)
        insertNode(root, 6)
        insertNode(root, 10)
        insertNode(root, 14)

        self.assertEqual(Solution().findCeilingFloor(root, 1), None)

def insertNode(root: TreeNode, num: int):
    if num > root.value:
        if root.right is None:
            root.right = TreeNode(num)
            return
        else:
            insertNode(root.right, num)
    if num < root.value:
        if root.left is None:
            root.left = TreeNode(num)
            return
        else:
            insertNode(root.left, num)


if __name__ == '__main__':
    unittest.main()
