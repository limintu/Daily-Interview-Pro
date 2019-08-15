class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        ans = [-1, -1]
        if nums is None or len(nums) == 0:
            return ans

        low = 0
        high = len(nums) - 1
        candidate = -1
        while low < high:
            mid = low + (high - low) // 2

            if target == nums[mid]:
                candidate = mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if nums[low] == target:
            ans[0] = low
        else:
            if candidate != -1:
                ans[0] = candidate
            else:
                return [-1, -1]

        low = 0
        high = len(nums) - 1
        candidate = -1

        while low < high:
            mid = low + (high - low) // 2

            if target == nums[mid]:
                candidate = mid
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        if nums[low] == target:
            ans[1] = low
        else:
            ans[1] = candidate

        return ans
