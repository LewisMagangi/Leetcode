# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        list_node = []

        while head:
            list_node.append(head.val)
            head = head.next
        list_str = ''.join(map(str, list_node))
        return int(list_str, 2)