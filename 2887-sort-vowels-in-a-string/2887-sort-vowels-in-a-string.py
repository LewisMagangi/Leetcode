class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        j = 0
        vowels = set('aeiouAEIOU')
        s_vowels_list = [i for i in s if i in vowels]
        sorted_list = sorted(''.join(s_vowels_list))

        for i in range(len(s[:])):
            if s[i] in vowels:
                s[i] = sorted_list[j]
                j += 1
        
        return ''.join(s)

        