class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        DigitsToChar = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations = ['']

        for digit in digits:
            new_combinations = []
            letters = DigitsToChar[int(digit) - 2]
            for prefix in combinations:
                for letter in letters:
                    new_combinations.append(prefix + letter)
            combinations = new_combinations
        return combinations
            