class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for candidate in candidates:
            for t in range(candidate, target + 1):
                for combination in dp[t - candidate]:
                    dp[t].append(combination + [candidate])
            
        return dp[target]