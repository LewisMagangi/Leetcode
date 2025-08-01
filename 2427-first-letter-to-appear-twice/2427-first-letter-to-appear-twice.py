from collections import defaultdict

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        1. create a hashmap = {letter: no of appearance}
        2. Iterate the first two appearances of a letter break and return the letter
        """
        letter_appearances = defaultdict(int)

        for letter in s:
            if letter in letter_appearances:
                return letter
            letter_appearances[letter] += 1