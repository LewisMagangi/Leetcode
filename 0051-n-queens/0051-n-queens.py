class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        diag1 = set()
        diag2 = set()
        cols = set()

        def backtrack(row, state):
            if row == n:
                solutions.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in state])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
            
                state.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1, state)

                state.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0, [])
        return solutions

        