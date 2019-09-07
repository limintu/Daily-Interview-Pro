import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        if nums is None or len(nums) == 0:
            return 0

        left, right = 0, 0
        sum_up = 0
        ans = sys.maxsize

        while right < len(nums):
            sum_up += nums[right]
            while sum_up >= s:
                ans = min(ans, right - left + 1)
                sum_up -= nums[left]
                left += 1

            right += 1

        return ans if ans != sys.maxsize else 0
