class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        color = [0] * numCourses

        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        def dfs(course):
            if color[course] == 1: # found a cycle (gray node)
                return False
            if color[course] == 2: # Already fully processed
                return True
            
            color[course] = 1 # Mark node(gray) meaning visited

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False
            
            color[course] = 2 # Mark as black (finished)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True