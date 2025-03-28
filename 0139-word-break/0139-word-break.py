from collections import deque

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = deque([0])
        visited = set()

        while queue:
            start = queue.popleft()

            if start == len(s):
                return True
            
            for word in wordDict:
                end = start + len(word)
                if end <= len(s) and s[start:end] == word and end not in visited:
                    queue.append(end)
                    visited.add(end)
        return False