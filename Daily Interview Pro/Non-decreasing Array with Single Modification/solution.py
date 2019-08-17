class Solution:
    def check(self, nums: list) -> bool :
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                if count > 1:
                    return False

                # modify nums[i-1] to a proper number
                if i - 1 == 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:  # or change the nums[i] to a proper number
                    nums[i] = nums[i - 1]

        return True
