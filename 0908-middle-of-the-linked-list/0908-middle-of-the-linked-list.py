# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head

        count = 0
        while curr:
            count += 1
            curr = curr.next

        middle_no = count // 2 + 1
        curr = head
        count = 1
        while curr:
            if count == middle_no:
                return curr
            curr = curr.next
            count += 1
        
        