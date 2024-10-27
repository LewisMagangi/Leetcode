from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        return nums_counter.most_common()[0][0]    