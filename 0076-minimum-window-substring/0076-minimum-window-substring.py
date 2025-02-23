from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t:
            return ""

        count_t = Counter(t)
        l, r = 0, 0
        required_chars = len(count_t)
        formed = 0
        window_count = {}

        res = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in count_t and window_count[char] == count_t[char]:
                formed += 1

            while l <= r and formed == required_chars:
                char = s[l]

                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)

                window_count[char] -= 1

                if char in count_t and window_count[char] < count_t[char]:
                    formed -= 1
                
                l += 1
            r += 1
        
        return "" if res[0] == float('inf') else s[res[1]:res[2] + 1]
