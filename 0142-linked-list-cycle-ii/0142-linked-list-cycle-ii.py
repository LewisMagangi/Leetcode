# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Ways to solve this:
        1. Hashset: Complexity  Time - O(n), Memory O(n)
        Initialize a hashset named seen and iterate through the linkedlist if 
        we find a val not seen we will add it to seen else we'll return the index of the first occurece 
        of the value in seen
        
        2.Use Floyd's Hare and Tortoise algorithm
        Initialize to pointers slow and fast and move the fast as twice as the slow which move on every elem
        Once slow == fast we'll figure out a way to find the index where the cycle begins
        because where the fast and slow meets isn't where the cycle begins
        .
        """
        seen = set()
        node = head
        while node:
            if node in seen:
                return node
            else:
                seen.add(node)
                node = node.next
        return None
