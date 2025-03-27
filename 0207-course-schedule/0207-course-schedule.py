class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        Prerequisite_map = { i:[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            Prerequisite_map[course].append(prerequisite)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if Prerequisite_map[course] == []:
                return True
            
            visited.add(course)

            for prerequisite in Prerequisite_map[course]:
                if not dfs(prerequisite):
                    return False
            
            visited.remove(course)
            Prerequisite_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True            
        