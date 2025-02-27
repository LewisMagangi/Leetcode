# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        I need to iterate through the linked list while appending the indexs
        in a hashset for constant lookup time
        and once i find an index that I've seen before I'll raise true else 
        false
        """
        node = head
        seen = set()
        while node:
            if node not in seen:
                seen.add(node)
                node = node.next
            else:
                return True
        return False