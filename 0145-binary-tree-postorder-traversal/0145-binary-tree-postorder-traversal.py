# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []

        node_list = []
        node_list += self.postorderTraversal(root.left)
        node_list += self.postorderTraversal(root.right)
        node_list.append(root.val)

        return node_list
        