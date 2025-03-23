from collections import deque

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(([], 0, 0))
        result = []

        while queue:
            path, total, index = queue.popleft()
            if total == target:
                result.append(path)
                continue
            if total > target or index == len(candidates):
                continue
            
            queue.append((path + [candidates[index]], total + candidates[index], index))
            queue.append((path, total, index + 1))
        
        return result
