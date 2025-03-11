from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        """
        Inorder Traversal - Root, Left, Right. This is the way the input root Node is traversed.
        I'll implement inorder traversal recursively and once I reach a next node I'll check if the right node is present if
        it is I'll replace it's val with the next val else the right(Node) will be set to Null.
        """
        if not root:
            return None
        
        queue = deque()
        queue.append(root)

        while queue:
            curr = None
            nxt = None

            for _ in range(len(queue)):
                if not curr:
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

                elif not nxt:
                    nxt = queue.popleft()
                    curr.next = nxt
                    if nxt.left:
                        queue.append(nxt.left)
                    if nxt.right:
                        queue.append(nxt.right)

                else:
                    curr = queue.popleft()
                    nxt.next = curr
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    nxt = curr
        return root