class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        state = []
        solutions = []
        self.search(state, solutions, n)
        return solutions

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        position = len(state)
        candidates = set(range(n))

        for row, col in enumerate(state):
            candidates.discard(col)
            distance = position - row
            candidates.discard(col + distance)
            candidates.discard(col - distance)
        return candidates

    def search(self, state, solutions, n):
        """
        Checks if a state is valid and if it is it add the state to the solutions
        """
        if self.is_valid(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return 

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def is_valid(self, state, n):
        """
        Checks if the new proposed position is valid ?
        """
        return len(state) == n

    def state_to_string(self, state, n):
        res = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            res.append(string)
        return res
        
        