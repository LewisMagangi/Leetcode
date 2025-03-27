# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        """ Helper function to push leftmost nodes to the stack
        """
        while root:
            self.stack.append(root)
            root = root.left

        

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None

        res = self.stack.pop()

        if res.right:
            self._leftmost_inorder(res.right)
        
        return res.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()