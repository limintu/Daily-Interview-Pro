class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invert(self, root):
        if root is None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invert(root.left)
        self.invert(root.right)

