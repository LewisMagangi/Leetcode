class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        for word in sorted(words, key=len):
            dp[word] = max(dp.get(word[:i] + word[i+1:], 0) + 1 for i in xrange(len(word)))

        return max(dp.values())
        