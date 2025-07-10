# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        def get_size(node):
            size = 0
            while node:
                size += 1
                node = node.next
            return size
        
        size = get_size(head)
        self.current = head

        def convert(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2

            left = convert(l ,mid - 1)
            root = TreeNode(self.current.val)
            self.current = self.current.next

            right = convert(mid + 1, r)

            root.left = left
            root.right = right
            return root

        return convert(0, size - 1) 
            
