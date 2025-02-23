class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, res = 0, len(nums) + 1
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != len(nums) + 1 else 0
