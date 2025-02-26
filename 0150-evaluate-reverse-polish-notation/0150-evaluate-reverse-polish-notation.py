class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        """
        Ways to solve this
        1. Use a stack approach

        Tranverse the stack once i encounter a symbol i'll pop the last two no's from the stack
        and do the 'evaluation = second_no expression first_no', 
        this should give us a new no that we will be stored as a string

        store the new no and proceed on c

        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        tokens = ["10","6","12","-11","*","/","*","17","+","5","+"]
        tokens = ["10","6","132","/","*","17","+","5","+"]
        tokens = ["10","6","132","/","*","17","+","5","+"]
        tokens = ["10","0","*","17","+","5","+"]
        tokens = ["0","17","+","5","+"]
        tokens = ["17","5","+"]
        tokens = ["22"]

        change this list of one str to an int.

        Append to the stack until i find the operator after which 
        i'll pop the 3 from the stack and append the evalution to the stack and proceed

        First logical error output is 12 instead of 22. This happened due to wrong div
        """
        operators = {
            '-': lambda a, b: a - b,
            '+': lambda a, b: a + b, 
            '/': lambda a, b: int(float (a) / b),
            '*': lambda a, b: a * b
            }
        stack = []

        for token in tokens:
            if token in operators:
                operator = token
                first_no = stack.pop() 
                second_no = stack.pop()
                evaluation = operators[operator](int(second_no), int(first_no))
                stack.append(evaluation)
            else:
                stack.append(token)
        return int(stack[0])
