from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        DigitsToChar = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        queue = deque([''])

        for digit in digits:
            level_size = len(queue)
            letters = DigitsToChar[digit]
            for _ in range(level_size):
                combinations = queue.popleft()
                for letter in letters:
                    queue.append(combinations + letter)
        return list(queue)
            