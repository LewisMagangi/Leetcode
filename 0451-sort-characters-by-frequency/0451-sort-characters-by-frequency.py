from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the frequency of each character
        count = Counter(s)
        
        # Sort characters by frequency in descending order
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        # Create the result string by repeating characters based on their frequency
        result = ''.join(char * freq for char, freq in sorted_items)
        
        return result
