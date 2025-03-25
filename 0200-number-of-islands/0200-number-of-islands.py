from collections import deque

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
        visited =  set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left
        islands = 0

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            
            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if (0 <= next_row < rows and 0 <= next_col < cols and
                        grid[next_row][next_col] == '1' and (next_row, next_col) not in visited):
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands