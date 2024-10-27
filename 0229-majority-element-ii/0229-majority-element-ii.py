from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums) // 3
        nums_counter = Counter(nums)
        elem = [nums for nums, count in nums_counter.items() if count > l]
        return elem
