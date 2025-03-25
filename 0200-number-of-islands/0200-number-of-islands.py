class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left
        islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col]  == '0':
                return
            grid[row][col] = '0'
            dfs(row + 1, col) # down
            dfs(row - 1, col) # up
            dfs(row, col + 1) # right
            dfs(row, col - 1) # left


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1
        return islands