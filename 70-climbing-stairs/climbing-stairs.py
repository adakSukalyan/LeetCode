class Solution:
    def count(self, i, n, dp):
        if i == n:
            return 1
        if i > n:
            return 0
        if dp[i] != -1:
            return dp[i]
        dp[i] = self.count(i + 1, n, dp) + self.count(i + 2, n, dp)
        return dp[i]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        return self.count(0, n, dp)