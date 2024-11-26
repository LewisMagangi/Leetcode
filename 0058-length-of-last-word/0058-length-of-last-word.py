class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s) - 1
        l = 0
        
        while n >= 0 and s[n] == " ":
            n -= 1

        while n >= 0 and s[n] != " ":
            n -= 1
            l += 1

        return l 
        