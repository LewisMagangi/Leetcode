class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        current_sum = 0
        min_sub = 10 ** 6

        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum >= target:
                min_sub = min(min_sub, r - l + 1)
                current_sum -= nums[l]
                l += 1
            
        return min_sub if min_sub != (1000000) else 0

            
         

        