class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip().rsplit(' ', 1)
        return len(s[-1])
        