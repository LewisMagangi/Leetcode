# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        """
        K <= length of ListNode
        reverse nodes of the list K at a time.
        return modified list.

        Understanding the pproblem:
        Left out k nodes ie in the first example [1,2,3,4,5], k = 2.
        2 is not a multiple of 5 so left out k digits at a time to all digits that are multiple of 2.
        The end digits should remain as it is.
        ie reverse the first k digits 
        then the next k digits and so on. Note that the digit in the ListNode
        are ascending.

        Input: head = [1,2,3,4,5], k = 2
        Output: [2,1,4,3,5]

        Input: head = [1,2,3,4,5], k = 3
        Output: [3,2,1,4,5]

        Steps:
        Start at the end of the list and once i find the first multiple of k   start at the 
        i'll reverse all the next digits k at a time until i've exhausted the list.
        simple function to reverse the list.
            - store the next digit
            - detach the current tail from the next digit
            - link the current tail to the previous head
            - link the next digit to the current tail
        """

        dummy = ListNode(0, head)
        prevgroup = dummy

        def getkth(curr, k):
            """
            Helper to find kth node after curr
            """
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = getkth(prevgroup, k)
            if not kth:
                break

            nextgroup = kth.next
            prev, curr = kth.next, prevgroup.next

            while curr != nextgroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prevgroup.next
            prevgroup.next = kth
            prevgroup = temp
        return dummy.next