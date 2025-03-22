class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        res = []
        DigitsToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, curr_str):
            if i == len(digits):
                res.append(curr_str)
                return
        
            for c in DigitsToChar[digits[i]]:
                backtrack(i + 1, curr_str + c)

        backtrack(0, '') 
        return res