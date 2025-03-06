# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def valid(node, min_val=float('-inf'), max_val=float('inf')):
            if node is None:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (valid(node.left, min_val, node.val) and valid(node.right, node.val, max_val))

        return valid(root)

        
        