class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        
        while l < r:
            if nums[l] == target:
                return l
            elif nums[l] < target:
                l += 1
            else:
                r -= 1
        return l
                

        