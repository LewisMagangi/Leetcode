class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_to_index = {}

        for index, no in enumerate(nums):
            complement = target -  no
            if complement in nums_to_index:
                return [nums_to_index[complement], index]
            nums_to_index[no] = index