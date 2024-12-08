class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        
        max_len = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen: 
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len 
                        