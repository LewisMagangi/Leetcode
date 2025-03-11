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
        This function uses level-order (BFS) traversal to connect each node's 'next' pointer to its immediate right neighbor.
        It processes nodes level by level using a queue. For each level, it iterates through all nodes, linking the previous node
        to the current one, and enqueues the child nodes for the next level.
        """
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root