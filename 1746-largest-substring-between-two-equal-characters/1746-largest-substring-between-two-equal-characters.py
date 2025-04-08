class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        v1 = [-1] * 26
        v2 = [-1] * 26
        max_len = -1

        for i in range(len(s)):
            temp = ord(s[i]) - ord('a')

            if v1[temp] == -1:
                v1[temp] = i
            else:
                v2[temp] = i
                max_len = max(max_len, v2[temp] - v1[temp] - 1)
                
        return max_len
        