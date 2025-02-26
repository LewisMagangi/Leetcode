"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None

        Should check if minstack is empty if it is i should add val if it isn't i should check 
        if the last min is less than val
        """
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
    
        

    def pop(self):
        """
        :rtype: None

        Poping the min value makes the list empty find a way to update next min value
        Poping the min value should retrieve the min from the minstack too

        If I'm popping the stack and that value is the min i should pop the minstack too and then if I'm
        pushing a value and that value is equal or less to the min i should update the min too 

        """
        if self.min_stack and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        return None
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()