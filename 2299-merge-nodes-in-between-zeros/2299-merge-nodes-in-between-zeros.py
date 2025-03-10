# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        tail = dummy = ListNode()

        while curr.next: 
            node = ListNode(0)
            while curr.next.val != 0:
                node.val += curr.next.val
                curr = curr.next
            tail.next = node
            tail = tail.next
            curr = curr.next
        return dummy.next

            
        