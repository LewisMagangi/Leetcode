class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memoization = {}

        def dp(i, j):
            if len(word1) == i:
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memoization:
                return memoization[(i, j)]
            
            if word1[i] == word2[j]:
                memoization[(i, j)] = dp(i + 1, j + 1)
            
            else:
                insert = dp(i, j + 1)  # Insert operation
                delete = dp(i + 1, j)  # Delete operation
                replace = dp(i + 1, j + 1)  # Replace operation
                memoization[(i, j)] = 1 + min(insert, delete, replace)

            return memoization[(i, j)]

        return dp(0, 0)