class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        first_occurence = [-1] * 26

        for i, char in enumerate(s):
            index = ord(char) - ord('a')
        
            if first_occurence[index] == -1:
                first_occurence[index] = i  
            else:
                actual_distance = i - first_occurence[index] - 1
                if actual_distance != distance[index]:
                    return False
        return True