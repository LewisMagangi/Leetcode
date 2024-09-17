class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0

        while i < len(s):
            if s[i] == 'i':
                s = s[:i][::-1] + s[i + 1:]
            else:
                i += 1

        s = [i for i in s if i != 'i']
        return ''.join(s)