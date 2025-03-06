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
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        first = head
        for _ in range(k - 1):
            first = first.next

        second = head        
        for _ in range(count - k):
            second = second.next

        first.val, second.val = second.val, first.val
        return head