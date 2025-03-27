from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacency_list = { i:[] for i in range(numCourses)}

        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed_courses = 0

        while queue:
            course = queue.popleft()
            processed_courses += 1

            for dependent in adjacency_list[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        return processed_courses == numCourses