class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        shortest_word = min(strs, key=len)

        for i in range(len(shortest_word)):
            for string in strs:
                if string[i] != shortest_word[i]:
                    return shortest_word[:i]
        return shortest_word