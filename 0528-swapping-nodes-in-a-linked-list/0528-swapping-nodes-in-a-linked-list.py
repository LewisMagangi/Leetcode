# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        first = head

        for _ in range(k - 1):
            first = first.next
        
        second = head
        curr = first
        while curr.next:
            curr = curr.next
            second = second.next

        first.val, second.val = second.val, first.val
       
        return head