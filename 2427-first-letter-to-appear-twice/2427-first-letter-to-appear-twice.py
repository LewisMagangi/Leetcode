class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        for i in s:
            if i in l:
                return i
            else:
                l.append(i)