class Solution:
    def findSequence(self, nums: list) -> list:
        # assume the range of number is 0-9
        count = [0] * 10
        diff_number_count = 0
        left, right = 0, 0
        ans = 0

        while right < len(nums):
            num = nums[right]

            if count[num] == 0:
                diff_number_count += 1

            count[num] += 1

            while diff_number_count > 2:
                to_remove = nums[left]
                if count[to_remove] == 1:
                    diff_number_count -= 1

                count[to_remove] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans
