class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ''

        start, max_length = 0, 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindromes (centered at s[i])
            left1, right1 = expandAroundCenter(i, i)
            # Even-length palindromes (centered between s[i] and s[i+1])
            left2, right2 = expandAroundCenter(i, i + 1)

            if right1 - left1 > max_length:
                start, max_length = left1, right1 - left1
            if right2 - left2 > max_length:
                start, max_length = left2, right2 - left2
                
        return s[start:start + max_length + 1]

        