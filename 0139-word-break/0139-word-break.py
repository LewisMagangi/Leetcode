class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memoization = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memoization:
                return memoization[i]

            for word in wordDict:
                if s[i:].startswith(word):
                    if dfs(i + len(word)):
                        memoization[i] = True
                        return True
            
            memoization[i] = False
            return False
        return dfs(0)