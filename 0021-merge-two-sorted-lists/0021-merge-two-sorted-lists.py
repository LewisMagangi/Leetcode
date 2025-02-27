# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        iterate through the nodes and append on stack if the
        Note that the list len is not always equal

        check if l1 and l2 are present.If l1 only pre append the
        whole of the of rem l1 same to l2. Or check both and append only if one is present so the absent one
        isn't appended automatically.Iterate through both linked-lists while checking which head is
        greater and inserting the smaller node. if they are equal insert both.

        you can append in place or use another list. mem complexity is O(1) O(n) respectively. Time comp is O(n) in both.
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2

        return dummy.next
