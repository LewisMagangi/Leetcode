# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curra, currb = headA, headB

        while curra != currb:
            curra = curra.next if curra else headB
            currb = currb.next if currb else headA
        return curra  
        
        