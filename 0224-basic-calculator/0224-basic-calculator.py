class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(index):
            stack = []
            num = 0
            sign = 1

            while index < len(s):
                char = s[index]

                if char.isdigit():
                    num = num * 10 + int(char)
                
                elif char in '+-':
                    stack.append(sign * num)
                    num = 0
                    sign = 1 if char == '+' else -1
                
                
                elif char == '(':
                    num, index = helper(index + 1)

                elif char == ')':
                    stack.append(sign * num)
                    return sum(stack), index
                
                index += 1

            stack.append(sign * num)
            return sum(stack)
        return helper(0)
        