class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)

        left, right = 0, len(s) - 1
        for _ in range(len(s) // 2):
            
            while left < right and s[right] not in vowels:
                right -= 1
            while right > left and s[left] not in vowels:
                left += 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
        return ''.join(s)