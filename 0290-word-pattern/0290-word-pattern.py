class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        return len(p) == len(s.split()) and len(set(zip(p, s.split()))) == len(set(p)) == len(set(s.split()))
        