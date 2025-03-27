class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        # Step 1: Build the graph (adjacency list)
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # Step 2: Variables to track visited nodes
        visited = set()   # Nodes that have been fully processed
        recStack = set()  # Nodes currently in the recursion stack
        order = []        # Stores topological order

        # Step 3: DFS function to detect cycles and process nodes
        def dfs(course):
            if course in recStack:
                return False  # Cycle detected
            if course in visited:
                return True   # Already processed
            
            recStack.add(course)  # Add to recursion stack
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False  # If cycle found, return False
            
            recStack.remove(course)  # Remove from recursion stack
            visited.add(course)      # Mark as fully processed
            order.append(course)     # Append to result (postorder)
            return True

        # Step 4: Perform DFS for each course
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []  # If a cycle is detected, return empty list
        
        return order[::-1]  # Reverse the order for correct topological sorting