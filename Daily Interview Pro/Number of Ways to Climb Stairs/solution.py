class Solution:
    def staircase(self, n):
        steps = [0 for _ in range(n+1)]
        steps[0] = 1
        steps[1] = 1

        for i in range(2, n + 1):
            steps[i] = steps[i-1] + steps[i-2]

        return steps[-1]
