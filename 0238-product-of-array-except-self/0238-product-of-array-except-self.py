class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length

        prefix = 1 

        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for j in range(length - 1, -1, -1):
            result[j] *= suffix
            suffix *= nums[j]

        return result