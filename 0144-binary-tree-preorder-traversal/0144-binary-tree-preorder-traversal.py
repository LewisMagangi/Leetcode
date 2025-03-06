# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []

        nodes_list = [root.val]
        nodes_list += self.preorderTraversal(root.left)
        nodes_list += self.preorderTraversal(root.right)

        return nodes_list
