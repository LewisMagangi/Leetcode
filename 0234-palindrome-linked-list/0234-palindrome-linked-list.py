# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr = head
        list_node = []
        while curr:
            list_node.append(curr.val)
            curr = curr.next
        return list_node == list_node[::-1]

        