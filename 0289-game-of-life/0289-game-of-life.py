class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def Countneighbors(row, col):
            neighbor = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if ((i == row and j == col) or i < 0 or j < 0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1, 3]:
                        neighbor += 1

            return neighbor


        for row in range(rows):
            for col in range(cols):
                neighbor = Countneighbors(row, col)

                if board[row][col] == 1:
                    if neighbor in [2, 3]:
                        board[row][col] = 3
                elif board[row][col] == 0 and neighbor == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1

        