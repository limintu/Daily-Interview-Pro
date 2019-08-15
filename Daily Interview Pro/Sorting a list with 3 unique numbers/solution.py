class Solution:
    def sortNums(self, nums: list) -> list:
        # ans = self.twoPassSolution(nums)
        ans = self.onePassSolution(nums)

        return ans

    def onePassSolution(self, nums: list) -> list:
        left, right = 0, len(nums) - 1

        i = 0
        while i <= right:
            num = nums[i]
            if num == 1:
                self.swap(nums, i, left)
                left += 1
                i += 1
            elif num == 3:
                self.swap(nums, i, right)
                right -= 1
            else:
                i += 1

        return nums

    def swap(self, nums: list, i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def twoPassSolution(self, nums: list) -> list:
        count = [0 for i in range(4)]

        for n in nums:
            count[n] += 1

        ans = []
        for i, num in enumerate(count):
            if num > 0:
                n = num
                while n > 0:
                    ans.append(i)
                    n -= 1

        return ans


# print(Solution().twoPassSolution([3, 3, 2, 1, 3, 2, 1]))
