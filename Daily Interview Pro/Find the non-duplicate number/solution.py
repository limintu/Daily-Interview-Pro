class Solution:
    def singleNumber(self, nums: list) -> int:
        n = 0
        for num in nums:
            n ^= num

        return n
