from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left
        area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row, col):
            area = 1
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if (0 <= next_row < rows and 0 <= next_col < cols and
                        grid[next_row][next_col] == 1 and (next_row, next_col) not in visited):
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
                        area += 1
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, bfs(row, col))
        return max_area


        