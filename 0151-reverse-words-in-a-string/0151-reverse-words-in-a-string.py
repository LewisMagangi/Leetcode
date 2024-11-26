class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = s.split()
        c = c[::-1]
        return ' '.join(c)
