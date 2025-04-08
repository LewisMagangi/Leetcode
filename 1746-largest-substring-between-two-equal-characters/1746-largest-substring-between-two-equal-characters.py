class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_index = {}
        max_len = -1

        for i, char in enumerate(s):
            if char in first_index:
                max_len = max(max_len, i - first_index[char] - 1)
            else:
                first_index[char] = i

        return max_len        
        