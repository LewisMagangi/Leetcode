# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node, res):
            if not node:
                return 0
            
            if node.left or node.right:
                res += 1
            return dfs(node.left, res) + dfs(node.right, res) + 1

        return dfs(root, 0)
        