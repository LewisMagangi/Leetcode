class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_set = set(nums)

        for i in range(1, len(nums) + 2):
            if i not in n_set:
                return i