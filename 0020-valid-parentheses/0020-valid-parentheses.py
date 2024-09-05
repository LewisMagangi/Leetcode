class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_dict = {'(':')', '{':'}', '[':']'}

        stack = []

        for i in s:
            if i in s_dict.keys():
                stack.append(i)
            elif i in s_dict.values():
                if not stack or s_dict[stack.pop()] != i:
                    return False
        return not stack
