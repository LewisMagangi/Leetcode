# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        while curr and curr.next:
            x = curr.val
            y = curr.next.val
            res = gcd(x, y)

            new_node = ListNode(res, curr.next)
            curr.next = new_node

            curr = curr.next.next
        return head

        