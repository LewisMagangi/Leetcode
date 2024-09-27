class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            if (nums[r] + nums[l]) < target:
                l += 1
            elif (nums[r] + nums[l]) > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        