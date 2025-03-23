class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        column = set()
        negative_diagonal = set()
        positive_diagonal = set()

        self.result = 0

        def backtrack(r):
            if r == n:
                self.result += 1
                return
        
            for c in range(n):
                if c in column or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                    continue
                
                column.add(c)
                positive_diagonal.add(r + c)
                negative_diagonal.add(r - c)
                backtrack(r + 1)
                column.remove(c)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)
        backtrack(0)
        return self.result