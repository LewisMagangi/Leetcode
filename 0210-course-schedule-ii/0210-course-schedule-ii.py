from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacency_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            in_degree[course] += 1
        
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for dependent in adjacency_list[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        if len(order) == numCourses:
            return order
        return []