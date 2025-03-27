class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r  # Define top and bottom boundaries

                # Store the top-left value
                topleft = matrix[top][l + i]

                # Move bottom-left to top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right to bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right to bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move stored top-left to top-right
                matrix[top + i][r] = topleft

            # Move to the next inner matrix
            r -= 1
            l += 1