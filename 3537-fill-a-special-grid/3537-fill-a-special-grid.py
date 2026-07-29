class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[0]]

        size = 2 ** n

        grid = [[0] * size for _ in range(size)]

        def fill(position, counter):
            i, j = position

            # top right
            grid[i][j + 1] = counter
            counter += 1

            # bottom right
            grid[i + 1][j + 1] = counter
            counter += 1

            # bottom left
            grid[i + 1][j] = counter
            counter += 1

            # top left
            grid[i][j] = counter
            counter += 1

            return counter

        def next_position(position, half):
        
            i, j = position
            
            top_right = (i, j + half)
            bottom_right = (i + half, j + half)
            bottom_left = (i + half, j)
            top_left = (i, j)

            return [
                top_right,
                bottom_right, 
                bottom_left,
                top_left,
            ]
            

        def run(position, size, counter):
            if size == 2:
                return fill(position, counter)

            half = size // 2
            
            positions = next_position(position, half)

            for position in positions:
                counter = run(position, half, counter)

            return counter

        counter = 0
        run((0,0), size, counter)
            
        return grid
            

            