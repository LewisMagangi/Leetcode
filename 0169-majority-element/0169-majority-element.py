from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        most_common_nums = nums_counter.most_common()
        return most_common_nums[0][0]
        