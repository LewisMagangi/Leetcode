class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                for first in dp[j]:
                    for second in dp[i - 1 - j]:
                        dp[i].append('(' + first + ')' + second)
        return dp[n]