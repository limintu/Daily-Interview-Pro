class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Solution:
    def findCeilingFloor(self, root: TreeNode, k: int, floor: TreeNode = None, ceil: TreeNode = None):
        if root is None:
            if floor is None or ceil is None:
                return None
            else:
                return [floor.value, ceil.value]
        if root.value == k:
            return [k, k]

        if k < root.value:
            ceil = root
            return self.findCeilingFloor(root.left, k, floor, ceil)
        else:
            floor = root
            return self.findCeilingFloor(root.right, k, floor, ceil)
