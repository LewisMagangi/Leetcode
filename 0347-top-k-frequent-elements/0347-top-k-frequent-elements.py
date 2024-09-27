from collections import Counter 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)

        sorted_items = count.most_common(k)

        result = [item for item, count in sorted_items]

        return result


