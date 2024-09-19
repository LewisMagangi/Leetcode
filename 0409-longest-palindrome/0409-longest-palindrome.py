from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        ls = len(s)
        count = Counter(s)
        if ls == 1:
            return 1
        for value in count.values():
            if value % 2 == 0:
                result += value
            else:
                result += value - 1

        if any(value % 2 != 0 for value in count.values()):
            result += 1
        return result



        