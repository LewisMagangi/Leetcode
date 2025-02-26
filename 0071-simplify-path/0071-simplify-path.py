

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        filenames = [filename for filename in path.split('/') if filename]

        for filename in filenames:
            if filename == '..':
                if stack:
                    stack.pop()
            elif filename != '.':
                stack.append(filename)
        return '/' + '/'.join(stack)