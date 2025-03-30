class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return 0

        dp = [0] * cols

        dp[0] = 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]

        return dp[-1]
        