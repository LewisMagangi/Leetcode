class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def ispalindrome(x):
            return x == x[::-1]
        s = list(s)
        l , r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return ispalindrome(s[l + 1 : r + 1]) or ispalindrome(s[l : r])
            l += 1
            r -= 1
        return True



        