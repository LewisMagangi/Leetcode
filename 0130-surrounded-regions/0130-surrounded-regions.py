from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0

        rows, cols = len(board), len(board[0])
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)] # down, up, right, left
        visited = set()

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            board[row][col] = 'S'

            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if (0 <= next_row < rows and 0 <= next_col < cols and board[next_row][next_col] == 'O'
                        and (next_row, next_col) not in visited):
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
                        board[next_row][next_col] = 'S'

        # Step 1: Start BFS from all 'O's on the border
        for r in range(rows):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][cols - 1] == 'O':
                bfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[rows - 1][c] == 'O':
                bfs(rows - 1, c)
        
        # Step 2: Flip surrounded 'O's to 'X' and safe 'S' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

        