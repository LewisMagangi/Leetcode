# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]

        iterate through the linked list until i 
        reach at pos left and reverse until pos right.
        """
        dummy = ListNode(0, head)
        curr = head
        leftprev = dummy

        for i in range(left - 1):
            leftprev = curr
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        leftprev.next.next = curr
        leftprev.next = prev
        return dummy.next

        