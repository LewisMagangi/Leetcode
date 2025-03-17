class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = [0]
        
        while len(word) < k:
            word.extend([(x + 1) % 26 for x in word])
        return chr(ord('a') + word[k - 1])


        