class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dp[row][col] = 0
                elif row == 0 and col == 0:
                    continue
                else:
                    dp[row][col] = (dp[row - 1][col] if row > 0 else 0) + (dp[row][col - 1] if col > 0 else 0)

        return dp[rows - 1][cols - 1]
        