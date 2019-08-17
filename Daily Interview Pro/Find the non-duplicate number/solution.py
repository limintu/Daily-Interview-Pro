class Solution:
    def singleNumber(self, nums: list) -> int:
        x = 0
        for num in nums:
            x ^= num

        return x

