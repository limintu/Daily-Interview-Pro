class Solution:
    def findPythagoreanTriplets(self, nums: list) -> bool:
        nums.sort()
        nums = [num for num in map(lambda x: x * x, nums)]

        for i in range(len(nums)-1, 1, -1):
            target = nums[i]

            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    return True

                if nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return False
