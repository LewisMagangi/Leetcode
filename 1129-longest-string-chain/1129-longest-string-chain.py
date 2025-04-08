class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        max_chain_length = 1
        dp = {}

        for word in words:
            dp[word] = 1

            for j in range(len(word)):
                predecessor = word[:j] + word[j+1:]
                
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
                
            max_chain_length = max(max_chain_length, dp[word])
        
        return max_chain_length