from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_r = Counter(ransomNote)
        count_m = Counter(magazine)

        """
        check if all the letters in raN are in mag and if their respective counts 
        are equal to the count of the same letters in mag
        """
        for key, value in count_r.items():
            if key in count_m and count_m[key] >= value:
                continue
            else:
                return False
        return True
