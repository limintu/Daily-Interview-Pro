class Solution:
    def num_ways(self, m, n):
        dp = [[0] * n for _ in range(m)]

        for i in range(len(dp)):
            dp[i][0] = 1

        for j in range(1, len(dp[0])):
            dp[0][j] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

