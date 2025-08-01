class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        first_occurence = {}

        for i, char in enumerate(s):
            if char in first_occurence:
                actual_distance = i - first_occurence[char] - 1
                if actual_distance != distance[ord(char) - ord('a')]:
                    return False
            else:
                first_occurence[char] = i
        return True