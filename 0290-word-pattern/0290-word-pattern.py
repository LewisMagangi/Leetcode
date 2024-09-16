class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(p) != len(s.split()):
            return False
        return len(set(zip(p, s.split()))) == len(set(p)) == len(set(s.split()))
        