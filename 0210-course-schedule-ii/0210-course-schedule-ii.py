class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)

        color = [0] * numCourses  # 0: white, 1: gray, 2: black
        order = []
        valid = [True]  # Use a list to modify inside dfs()

        def dfs(node):
            if color[node] == 1:
                valid[0] = False  # Cycle detected
                return
            if color[node] == 2:
                return  # Already processed
            
            color[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                dfs(neighbor)
            color[node] = 2  # Mark as processed
            order.append(node)

        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)
        
        if not valid[0]:
            return []
        return order[::-1]  # Reverse to get topological order
