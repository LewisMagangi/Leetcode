class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i :[] for i in range(numCourses)}

        for destination, source in prerequisites:
            graph[source].append(destination)
        
        state = [0] * numCourses
        order = []
        valid = [True]

        def dfs(course):
            if not valid[0]:
                return

            state[course] = 1
            
            for neighbor in graph[course]:
                if state[neighbor] == 0:
                    dfs(neighbor)
                elif state[neighbor] == 1:
                    valid[0] = False
            state[course] = 2
            order.append(course)

        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)

        if not valid[0]:
            return []
        return order[::-1]