class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        matrix = [[int(cell) for cell in row] for row in matrix]
        
        rows, cols = len(matrix), len(matrix[0])

        memoization = {}

        max_side = 0

        def dp(row, col):
            """ Recursive function to compute the largest square ending at (i, j)
            """
            if row < 0 or col < 0:
                return 0
            
            if (row, col) in memoization:
                return memoization[(row, col)]
            
            if matrix[row][col] == 0:
                memoization[(row, col)] = 0
                return 0
            
             # Recursive case: Take the min of left, top, and top-left neighbors + 1
            memoization[(i, j)] = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
            return memoization[(i, j)]

        for i in range(rows):
            for j in range(cols):
                max_side = max(max_side, dp(i, j))
        
        max_area = max_side * max_side
        return max_area    



        