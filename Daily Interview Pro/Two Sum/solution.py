class Solution:
    def two_sum(self, nums: list, k: int) -> bool:
        elements = set()

        for num in nums:
            if num in elements:
                return True
            else:
                elements.add(k - num)

        return False
