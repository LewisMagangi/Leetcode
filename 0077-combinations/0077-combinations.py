class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        dp = [[[]for _ in range(k + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = [[]]

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j][:]
                for comb in dp[i - 1][j - 1]:
                    dp[i][j].append(comb + [i])
                
        return dp[n][k]