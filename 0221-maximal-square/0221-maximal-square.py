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

        max_side = 0

        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]) + 1
                    max_side = max(max_side, dp[row][col])
        max_area = max_side * max_side
        return max_area

        