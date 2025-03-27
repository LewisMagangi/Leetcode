class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_stack = []  # Stack for previous results before '('
        op_stack = []    # Stack for signs before '('
        num = 0          # Current number
        result = 0       # Running total result
        sign = 1         # 1 for '+', -1 for '-'

        for char in s:
            if char.isdigit():  # Build number
                num = num * 10 + int(char)
            elif char in ["+", "-"]:  # Apply previous number and change sign
                result += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":  # Push current result & sign onto stack
                num_stack.append(result)
                op_stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":  # Complete parentheses evaluation
                result += sign * num  # Add last number before ')'
                num = 0
                result *= op_stack.pop()  # Apply sign before '('
                result += num_stack.pop()  # Add result before '('

        return result + (sign * num)  # Add last number if any
