class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return [i.lower() for i in s if i.isalnum()] == [i.lower() for i in s if i.isalnum()][::-1]