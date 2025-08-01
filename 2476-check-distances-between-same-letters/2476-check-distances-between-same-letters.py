from collections import defaultdict

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        string_indices_difference = defaultdict(int)

        for index, letter in enumerate(s):
            if letter in string_indices_difference:
                actual_distance = index - (string_indices_difference[letter] + 1)
                expected_distance = distance[ord(letter) - ord('a')]
                if actual_distance != expected_distance:
                    return False
            else:
                string_indices_difference[letter] = index
        return True