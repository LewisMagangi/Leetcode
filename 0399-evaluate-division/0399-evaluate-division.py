from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj_list = defaultdict(list)

        for i, equation in enumerate(equations):
            a, b = equation
            
            adj_list[a].append([b, values[i]])
            adj_list[b].append([a, 1 / values[i]])

        def bfs(source, target):
            if source not in adj_list or target not in adj_list:
                return -1
            
            queue, visited = deque(), set()
            queue.append([source, 1])
            visited.add(source)

            while queue:
                n, w = queue.popleft()
                if n == target:
                    return w
                
                for neighbor, weight in adj_list[n]:
                    if neighbor not in visited:
                        queue.append([neighbor, w * weight])
                        visited.add(neighbor)
            return -1
        return [bfs(query[0], query[1]) for query in queries]